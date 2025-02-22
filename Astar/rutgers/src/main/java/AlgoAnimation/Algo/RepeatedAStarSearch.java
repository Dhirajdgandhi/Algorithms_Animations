package AlgoAnimation.Algo;


import AlgoAnimation.Entity.BlockNode;
import AlgoAnimation.Entity.NodeBase;
import AlgoAnimation.Entity.XY;
import AlgoAnimation.UI.MainScreen;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.*;
//import com.spring.boot.PriorityQueue;

import static AlgoAnimation.Utility.Constants.Constant.*;
import static AlgoAnimation.Utility.MathsCalc.calculateManhattanDistance;

public class RepeatedAStarSearch{

    private static final Logger LOG = LoggerFactory.getLogger(RepeatedAStarSearch.class.getName());

    private int MAX_X, MAX_Y;

    private GridWorld<Integer> gridWorld;
    private PriorityQueue<NodeBase> openList;
    private LinkedList<XY> closedList;
    private XY initialCell, goalCell;
    private int expandedNodes = 0;
    private Map<XY, NodeBase> stateGridWorld;
    Thread currentThread;

    public RepeatedAStarSearch() {
    }

    public RepeatedAStarSearch(GridWorld<Integer> gridWorld, XY initialCell, XY goalCell) {
        this.MAX_Y = gridWorld.rowSize();
        this.MAX_X = gridWorld.colSize();
        this.gridWorld = gridWorld;
        this.initialCell = initialCell;
        this.goalCell = goalCell;

        // Star Node and Goal Node remains same for a problem irrespective of Forward/Backward Search
        NodeBase startNode = new BlockNode();
        startNode.setName("S");
        startNode.setDescription("The Game begins from this position");
        startNode.setGValue(0);
        startNode.setXy(initialCell);

        NodeBase goalNode = new BlockNode();
        goalNode.setName("G");
        goalNode.setDescription("The Game ends at this position");
        goalNode.setGValue(INFINITY);
        goalNode.setXy(goalCell);

        this.stateGridWorld = new HashMap();
        stateGridWorld.put(initialCell, startNode);
        stateGridWorld.put(goalCell, goalNode);

    }

    /**
     * The Repeated AStar Algorithm search Function
     *
     * @param isBackward True for backward search
     * @param adaptive   True for adaptive search
     */
    public int search(boolean isBackward, boolean adaptive) throws CloneNotSupportedException {
        List<XY> executedPath = new ArrayList();

        NodeBase goalNode = stateGridWorld.get(goalCell);
        NodeBase currentNode = stateGridWorld.get(initialCell);
        int counter = 0, cost = 0;
        currentThread = Thread.currentThread();

        while (!currentNode.equals(goalNode)) {
            counter += 1;

            // Same for B and F
            goalNode.setVisited(counter);
            currentNode.setVisited(counter);

            // Same for B and F
            openList = new PriorityQueue<>(50000, idComparator);
            closedList = new LinkedList<>();

            // See your visible cells and update your Visible World
            // Same for B and F
            for (XY neighbour : retrieveNeighbours(currentNode)) {
                if (isCellLegal(neighbour)) {
                    // If no Node created yet, then first create and add it to map
                    if (!stateGridWorld.containsKey(neighbour)) {
                        stateGridWorld.put(neighbour, new BlockNode(neighbour));
                    }
                    stateGridWorld.get(neighbour).setVisible(gridWorld.get(neighbour));
                }
            }

            // If Backward then switch the goal node and current node
            if (!isBackward) {
                computePath(currentNode, goalNode, counter);
            } else {
                computePath(goalNode, currentNode, counter);
            }

            if (!openList.isEmpty()) {
                NodeBase node = currentNode;
                List<XY> plannedPath = new ArrayList<>();

                if (!isBackward) { // Establish Reverse links from G->S to have S->G links
                    node = goalNode;
                    while (!node.equals(currentNode)) {
                        node.getParentNode().setChildNode(node);
                        node = node.getParentNode();
                    }
                }

                while (node != null) { // Travel S->G using appropriate linking and add path to plannedPath
                    plannedPath.add(node.getXy());
                    node = node.getLinkForPath(isBackward);
                }

                // Update Heuristic. The main part of Adaptive
                if (adaptive) {
                    int lengthOfPath = plannedPath.size() - 1;

                    for (XY i : plannedPath) {
                        stateGridWorld.get(i).setHValue(lengthOfPath--);
                    }
                }

                LOG.debug("Planned Path for execution is : {}", plannedPath);

                // Execution uses Real Grid World
                LOG.debug("Execution Begins");
                for (XY cell : plannedPath.subList(1, plannedPath.size())) {
                    if (isCellLegalAndUnBlocked(cell, true)) {
                        cost += 1;
                        executedPath.add(cell);
                        LOG.debug("Moved to Cell : {}", cell);
                        MainScreen.getCurrentGrid().get(cell.getY()).get(cell.getX()).changeColor(Color.YELLOW);
                        Text tileText = MainScreen.getCurrentGrid().get(cell.getY()).get(cell.getX()).getText();

                        String prevText = tileText.getText();
                        tileText.setText((prevText.isEmpty() ? "" : (prevText+","))+String.valueOf(cost));
                        tileText.setFill(Color.BLACK);
//                        try {
//                            currentThread.sleep(2000);
//                        } catch (InterruptedException e) {
//                            e.printStackTrace();
//                        }

                        currentNode = stateGridWorld.get(cell);
                    } else {
                        // Run AStar with currentNode again
                        break;
                    }
                }

            } else {
                LOG.info("NO PATH to target can be found.");
                return -1;
            }
        }

        LOG.info("Executed Path : {}", executedPath);
//        int executingStep = 1;
//        for(XY cell : executedPath){
//
//            executingStep+=1;
//        }
        return cost;
    }

    /**
     * AStar Algorithm to compute Path with Start and Goal node
     */
    private void computePath(NodeBase startNode, NodeBase goalNode, int counter) {
        startNode.setParentNode(null);
        startNode.setChildNode(null);
        startNode.setGValue(0); // Takes no cost to reach where we are
        if (startNode.getHValue() == 0) // Calculate Manhattan Distance if not previously calculated
            startNode.setHValue(calculateManhattanDistance(startNode.getXy(), goalNode.getXy()));
        startNode.calculateAndSetFValue(); // f = g + h

        openList.add(startNode);

        goalNode.setParentNode(null);
        goalNode.setChildNode(null);
        goalNode.setGValue(INFINITY);
        goalNode.calculateAndSetFValue();
        NodeBase currentNode = startNode;

        while (currentNode != null && goalNode.getGValue() > currentNode.getFValue()) {
            LOG.debug("Exploring Node : {} : {}", currentNode.getXy(), currentNode);
            expandedNodes += 1;

            //Remove he current Node that we explored from top of Open List
            openList.poll();
            closedList.add(currentNode.getXy());

            if(gridWorld.getGridWorld().get(currentNode.getXy().getX()).get(currentNode.getXy().getY()) != BLOCKED_CELL){
                MainScreen.getCurrentGrid().get(currentNode.getXy().getX()).get(currentNode.getXy().getY()).changeColor(Color.GREY);
            }
            for (XY neighbour : retrieveNeighbours(currentNode)) {
                if (isCellLegalAndUnBlocked(neighbour, false)) {

                    if (!stateGridWorld.containsKey(neighbour)) {
                        stateGridWorld.put(neighbour, new BlockNode(neighbour));
                    }
                    NodeBase neighbourNode = stateGridWorld.get(neighbour);

                    if (neighbourNode.getVisited() < counter) {
                        neighbourNode.setGValue(INFINITY);
                        neighbourNode.setVisited(counter);
                    }

                    if (neighbourNode.getGValue() > currentNode.getGValue() + 1) {// g' > g(s) + c(a,s) // c(a,s) = someGrid.get(currentNode.getXy())
                        neighbourNode.setGValue(currentNode.getGValue() + 1);
                        neighbourNode.setParentNode(currentNode);
                        if (neighbourNode.getHValue() == 0)
                            neighbourNode.setHValue(calculateManhattanDistance(neighbour, goalNode.getXy()));
                        neighbourNode.calculateAndSetFValue();

                        if (openList.contains(neighbourNode)) {
                            openList.remove(neighbourNode);// TODO: Improve from Linear Search and  write remove function
                        }
                        LOG.debug("Adding Neighbour to Open List : {}", neighbourNode);
                        openList.add(neighbourNode);

                        if(gridWorld.getGridWorld().get(currentNode.getXy().getX()).get(currentNode.getXy().getY()) != BLOCKED_CELL){
                            MainScreen.getCurrentGrid().get(neighbourNode.getXy().getY()).get(neighbourNode.getXy().getX()).changeColor(Color.GREEN);
                            Text tileText = MainScreen.getCurrentGrid().get(neighbourNode.getXy().getY()).get(neighbourNode.getXy().getX()).getText();
//                            String newText = new StringBuilder()
//                                    .append("\nF:")
//                                    .append(currentNode.getFValue())
//                                    .append("\nH:")
//                                    .append(currentNode.getHValue())
//                                    .append("\nG:")
//                                    .append(currentNode.getGValue())
//                                    .toString();
//                            tileText.setText(newText);
                            tileText.setFill(Color.BLACK);
                        }

                        try {
                            currentThread.sleep(2500);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }


                    }
                }
            }

            // Get the next Top of Open List if it's not empty
            if (!openList.isEmpty()) {
                currentNode = openList.peek();
            } else {
                currentNode = null;
            }
            LOG.debug("\n\n\n");
        }
    }

    /**
     * Retrieves Neighbour List
     */
    private List<XY> retrieveNeighbours(NodeBase node) {
        int x = node.getXy().getX();
        int y = node.getXy().getY();

        return new ArrayList<>(Arrays.asList(new XY(x, y + 1), new XY(x + 1, y), new XY(x, y - 1), new XY(x - 1, y)));
    }

    private Boolean isCellLegal(XY cell) {
        return cell.getX() >= MIN_X && cell.getX() < MAX_X && cell.getY() >= MIN_Y && cell.getY() < MAX_Y;
    }

    /**
     * Checks if given Cell is legal and blocked
     *
     * @param A Co-ordinates of the cell to be checked
     * @return True if the Cell is Legal and UnBlocked
     */
    private Boolean isCellLegalAndUnBlocked(XY A, boolean seeRealWorldValue) {
        if (isCellLegal(A)) {
            if (!stateGridWorld.containsKey(A)) stateGridWorld.put(A, new BlockNode(A));

            if (seeRealWorldValue) return gridWorld.get(A) != BLOCKED_CELL;
            else return stateGridWorld.get(A).getVisible() != BLOCKED_CELL;
        } else {
            return false;
        }
    }

    public int getExpandedNodes() {
        return expandedNodes;
    }

    //Comparator anonymous class implementation
    public static Comparator<NodeBase> idComparator = new Comparator<NodeBase>(){

        @Override
        public int compare(NodeBase c1, NodeBase c2) {
            int value = (c1.getFValue() - c2.getFValue());
            if(value==0){
                LOG.debug("Breaking tie between Node : {} and Node : {}", c1, c2);
                value = (c2.getGValue() - c1.getGValue());
            }
            LOG.debug("And {} wins", value>0 ? c2 : c1);
            return value;
        }
    };
}
