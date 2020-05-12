package com.spring.boot.architecture.hexagonal.frontend;

import com.spring.boot.architecture.hexagonal.entity.Transaction;
import com.spring.boot.architecture.hexagonal.services.TransactionService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/web")
public class WebConsumerImpl implements IConsumerPort {

    Logger LOG = LoggerFactory.getLogger(WebConsumerImpl.class);

    @Autowired
    TransactionService transactionService;

    @Override
    public int addTransaction(Transaction transaction) {
        LOG.info("Got request from WEB to add transaction : {}",transaction);
        int transactionId = transactionService.addTransaction(transaction);
        LOG.info("Response : {}",transactionId);
        return transactionId;
    }

    @Override
    public String viewTransaction(int transactionId) {
        LOG.info("Request from WEB to view transaction with ID : {}", transactionId);
        Transaction transaction = transactionService.viewTransaction(transactionId);
        LOG.info("Response : {}",transaction);
        return transaction.toString();
    }
}
