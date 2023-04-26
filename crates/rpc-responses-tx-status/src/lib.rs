use std::str::FromStr;

use derive_more::{From, Into};
use pyo3::prelude::*;
use serde::{Deserialize, Serialize};
use solana_sdk::transaction::TransactionError as TransactionErrorOriginal;
use solana_transaction_status::TransactionConfirmationStatus as TransactionConfirmationStatusOriginal;
use solders_macros::{common_methods, richcmp_eq_only};
use solders_rpc_response_data_boilerplate::response_data_boilerplate;
use solders_signature::Signature;
use solders_transaction_error::TransactionErrorType;
use solders_transaction_status::TransactionConfirmationStatus;

// the one in solana_client uses transaction_status
#[derive(Clone, Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
struct RpcConfirmedTransactionStatusWithSignatureOriginal {
    pub signature: String,
    pub slot: u64,
    pub err: Option<TransactionErrorOriginal>,
    pub memo: Option<String>,
    pub block_time: Option<i64>,
    pub confirmation_status: Option<TransactionConfirmationStatusOriginal>,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize, Clone, From, Into)]
#[pyclass(module = "solders.rpc.responses", subclass)]
pub struct RpcConfirmedTransactionStatusWithSignature(
    RpcConfirmedTransactionStatusWithSignatureOriginal,
);

response_data_boilerplate!(RpcConfirmedTransactionStatusWithSignature);

#[richcmp_eq_only]
#[common_methods]
#[pymethods]
impl RpcConfirmedTransactionStatusWithSignature {
    #[new]
    pub fn new(
        signature: Signature,
        slot: u64,
        err: Option<TransactionErrorType>,
        memo: Option<String>,
        block_time: Option<i64>,
        confirmation_status: Option<TransactionConfirmationStatus>,
    ) -> Self {
        RpcConfirmedTransactionStatusWithSignatureOriginal {
            signature: signature.to_string(),
            slot,
            err: err.map(|e| e.into()),
            memo,
            block_time,
            confirmation_status: confirmation_status.map(|c| c.into()),
        }
        .into()
    }

    #[getter]
    pub fn signature(&self) -> Signature {
        Signature::from_str(&self.0.signature).unwrap()
    }
    #[getter]
    pub fn slot(&self) -> u64 {
        self.0.slot
    }
    #[getter]
    pub fn err(&self) -> Option<TransactionErrorType> {
        self.0.err.clone().map(|e| e.into())
    }
    #[getter]
    pub fn memo(&self) -> Option<String> {
        self.0.memo.clone()
    }
    #[getter]
    pub fn block_time(&self) -> Option<i64> {
        self.0.block_time
    }
    #[getter]
    pub fn confirmation_status(&self) -> Option<TransactionConfirmationStatus> {
        self.0.confirmation_status.clone().map(|s| s.into())
    }
}
