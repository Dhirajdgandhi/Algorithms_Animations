// import visualization libraries {
const { Layout, LogTracer, Tracer, VerticalLayout, Array2DTracer, Array1DTracer } = require('algorithm-visualizer');
// }

// define tracer variables {
const array2dTracer = new Array2DTracer('Primality Testing');
const array1dTracer = new Array1DTracer('Random Number');
const array1dTracer2 = new Array1DTracer('K');
const logTracer = new LogTracer('Console');
// }

// define input variables
let N, D, S, X, I, Xsquare;

const messages = [
    ['N', 'D', 'S', 'X = pow(a, d) % n', 'X = X * X % n (Repeating for s times)'],
    [N, D, S, X, Xsquare],
    ['', '', '', '', I]
];

N = 59; K = 10;
// visualize {
Layout.setRoot(new VerticalLayout([array1dTracer2, array1dTracer, array2dTracer, logTracer]));
array2dTracer.set(messages);
array1dTracer.set([0]);
array1dTracer2.set([K]);

function patchSD(s, d){
    array2dTracer.patch(1, 2, s );
    array2dTracer.patch(1, 1, d );
    Tracer.delay();
    array2dTracer.depatch(1, 2 );
    array2dTracer.depatch(1, 1 );
}

// For the return values of this function, true means "probably prime" and false means "definitely composite."

function probablyPrime(n, k) {
    array2dTracer.patch(1, 0, n );
    Tracer.delay();
    array2dTracer.depatch(1, 0 );

    if (n === 2 || n === 3){
        logTracer.println(n + " is a prime");
        array2dTracer.selectRow(1, 0, 0);
        Tracer.delay();
        array2dTracer.deselectRow(1, 0, 0);
        return true;
    }

    if (n % 2 === 0 || n < 2){
        logTracer.println(n + " is an even and hence NOT a prime");
        array2dTracer.selectRow(1, 0, 0);
        Tracer.delay();
        array2dTracer.deselectRow(1, 0, 0);
        return false;
    }

    // Write (n - 1) as 2^s * d
    logTracer.println(" Writing (n-1) as 2^s * d ");
    var s = 0, d = n - 1;
    patchSD(s,d);

    while (d % 2 === 0) {
        d /= 2;
        ++s;
        patchSD(s,d);
    }

    WitnessLoop: do {
        array1dTracer2.patch(0, k);
        Tracer.delay();
        array1dTracer2.depatch(0 );

        // A base between 2 and n - 2
        var random = 2 + Math.floor(Math.random() * (n - 3));
        array1dTracer.patch(0, random);
        Tracer.delay();
        array1dTracer.depatch(0 );

        var x = Math.pow(random, d) % n;

        array2dTracer.patch(1, 3, x);
        Tracer.delay();
        array2dTracer.depatch(1, 3 );

        if (x === 1 || x === n - 1){
            logTracer.println("X was found to be "+ x + " and thus we perform Miller test again with a different random number");
            continue;
        }

        for (var i = s - 1; i--;) {
            array2dTracer.patch(2, 4, i);
            Tracer.delay();
            array2dTracer.depatch(2, 4 );

            x = x * x % n;

            array2dTracer.patch(1, 4, x);
            Tracer.delay();
            array2dTracer.depatch(1, 4 );

            if (x === 1){
                logTracer.println("x is " + x);
                logTracer.println("Hence Composite");
                return false;
            }
            if (x === n - 1){
                logTracer.println("x is " + x);
                logTracer.println("Hence Continuing the Main Loop with K");
                continue WitnessLoop;
            }

        }

        return false;
    } while (--k);

    return true;
}


// (function main() {
//     for( N = 1; N<100; N++){
        let primeOrNot = probablyPrime(N, K);
        array2dTracer.selectRow(1, 0, 0);
        Tracer.delay();
        array2dTracer.deselectRow(1, 0, 0);

        if (primeOrNot === false){
            logTracer.println(" Number is NOT a prime ")
        } else{
            logTracer.println(" Number might or might NOT be a prime ")
        }
    // }
// })();



