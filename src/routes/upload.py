from typing import Dict

from fastapi import HTTPException

from src.routes.app import app
from src.util.error_generator import ErrorGenerator
from src.util.invoice_process import InvoiceProcess


@app.post("/upload_invoice", tags=["Upload"])
def upload_invoice() -> Dict:
    """
    Route to upload all data contained in the input csv
    """
    try:
        invoice_process = InvoiceProcess()
        invoice_process.execute_invoice_process()

        response = {
            "message": "Invoices successfully generated",
            "runtime": invoice_process.runtime,
            "quantity_of_invoices": len(invoice_process.invoices_added),
        }

        return response
    except ErrorGenerator as error_generator:
        raise HTTPException(
            status_code=400,
            detail=str(error_generator.get_error_description()),
        )
    except Exception as other_error:
        raise HTTPException(status_code=400, detail=str(other_error))
