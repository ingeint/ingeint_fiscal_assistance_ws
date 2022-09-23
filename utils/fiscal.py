from . import ingeint_utils
import shutil
import os


def create_invoice(self):
    filename = "C:/PROCESANDO/" + self['file_name']
    with open(filename, 'w') as f:
        f.write("FACTURA:         " + self['document_number'] + "\n")
        f.write("FECHA:           " + str(self['invoiceDate']) + "\n")
        f.write("CLIENTE:         " + self['Customer'] + "\n")
        f.write("RIF:             " + self['Identification'] + "\n")
        f.write("DIRECCION1:      " + self['Address1'] + "\n")
        if 'Address2' in self:
            f.write("DIRECCION2:      " + self['Address2'] + "\n")
        else:
            f.write("DIRECCION2:      " + "\n")
        if 'Phone' in self:
            f.write("TELEFONO:        " + self['Phone'] + "\n")
        else:
            f.write("TELEFONO:        " + "\n")
        f.write(
            "DESCRIPCION                                                 COD          CANT.    IVA    PRECIO UNIT" + "\n")

        lines = self['invoice_lines']

        for line in lines:
            product_name = ingeint_utils.fill_product_name(line)
            product_code = ingeint_utils.fill_product_code(line)
            product_qty = str(line['qtyEntered']).ljust(6)
            product_tax = str(ingeint_utils.fill_product_tax(line)).ljust(4)
            product_price_unit = str(line['priceEntered']).rjust(13)
            f.write('{} {} {} {} {}'.format(product_name, product_code, product_qty, product_tax,
                                            product_price_unit) + "\n")
            if 'comment' in line:
                f.write(line['comment'] + "\n")

        f.write("SUB-TOTAL:".ljust(22) + str(self['sub_total']) + "\n")
        f.write("DESCUENTO:".ljust(24) + str(self['discount']) + "\n")
        f.write("TOTAL A PAGAR".ljust(22) + str(self['amount_total']) + "\n")

        payments = self['payment_methods']

        for payment in payments:
            if '01' in payment:
                f.write("EFECTIVO:".ljust(22) + str(payment['01']) + "\n")
                continue
            if '02' in payment:
                f.write("CHEQUES".ljust(22) + str(payment['02']) + "\n")
                continue
            if '03' in payment:
                f.write("TARJ / DEBITO:".ljust(22) + str(payment['03']) + "\n")
                continue
            if '04' in payment:
                f.write("TARJ / CREDITO:".ljust(22) + str(payment['04']) + "\n")
                continue
            if '05' in payment:
                f.write("Tranf en Bs:".ljust(22) + str(payment['05']) + "\n")
                continue
            if '06' in payment:
                f.write("Transf en USD".ljust(22) + str(payment['06']) + "\n")
                continue
            if '07' in payment:
                f.write("Transf EURO:".ljust(22) + str(payment['07']) + "\n")
                continue
            if '08' in payment:
                f.write("Efect USD:".ljust(22) + str(payment['08']) + "\n")
                continue
            if '09' in payment:
                f.write("Efect EURO:".ljust(22) + str(payment['09']) + "\n")
                continue
            if '10' in payment:
                f.write("Pago movil:".ljust(22) + str(payment['10']) + "\n")
                continue
            if '11' in payment:
                f.write("CREDITO:".ljust(22) + str(payment['11']) + "\n")
                continue

        f.write("NOTA 1:".ljust(7) + "\n")
        f.write("NOTA 2:".ljust(7) + "\n")
        f.write("NOTA 3:".ljust(7) + "\n")
        f.write("NOTA 4:".ljust(7))

        f.close()
        file_destination = 'C:/FACTURAS/' + self['file_name']
        shutil.move(filename,  file_destination)


def create_credit_note(self):
    filename = "C:/PROCESANDO/" + self['file_name']
    with open(filename, 'w') as f:
        f.write("DEVOLUCION:      " + self['document_number'] + "\n")
        f.write("FECHA:           " + str(self['invoiceDate']) + "\n")
        f.write("CLIENTE:         " + self['Customer'] + "\n")
        f.write("RIF:             " + self['Identification'] + "\n")
        f.write("DIRECCION1:      " + self['Address1'] + "\n")
        if 'Address2' in self:
            f.write("DIRECCION2:      " + self['Address2'] + "\n")
        else:
            f.write("DIRECCION2:      " + "\n")
        if 'Phone' in self:
            f.write("TELEFONO:        " + self['Phone'] + "\n")
        else:
            f.write("TELEFONO:        " + "\n")
        f.write(
            "DESCRIPCION                                                 COD          CANT.    IVA    PRECIO UNIT" + "\n")

        lines = self['invoice_lines']

        for line in lines:
            product_name = ingeint_utils.fill_product_name(line)
            product_code = ingeint_utils.fill_product_code(line)
            product_qty = str(line['qtyEntered']).ljust(6)
            product_tax = str(ingeint_utils.fill_product_tax(line)).ljust(4)
            product_price_unit = str(line['priceEntered']).rjust(13)
            f.write('{} {} {} {} {}'.format(product_name, product_code, product_qty, product_tax,
                                            product_price_unit) + "\n")
            if 'period' in line:
                f.write("PERIODO: " + line['period'] + "\n")

        f.write("SUB-TOTAL:".ljust(22) + str(self['sub_total']) + "\n")
        f.write("DESCUENTO:".ljust(24) + str(self['discount']) + "\n")
        f.write("TOTAL A PAGAR".ljust(22) + str(self['amount_total']) + "\n")
        f.write("EFECTIVO:".ljust(22) + str(self['amount_total']) + "\n")
        f.write("CHEQUES".ljust(22) + str(0.0) + "\n")
        f.write("TARJ / DEBITO:".ljust(22) + str(0.0) + "\n")
        f.write("TARJ / CREDITO:".ljust(22) + str(0.0) + "\n")
        f.write("Tranf en Bs:".ljust(22) + str(0.0) + "\n")
        f.write("Transf en USD:".ljust(22) + str(0.0) + "\n")
        f.write("Transf EURO:".ljust(22) + str(0.0) + "\n")
        f.write("Efect USD:".ljust(22) + str(0.0) + "\n")
        f.write("Efect EURO:".ljust(22) + str(0.0) + "\n")
        f.write("Pago movil:".ljust(22) + str(0.0) + "\n")
        f.write("CREDITO:".ljust(22) + str(0.0) + "\n")
        f.write("NOTA 1:" .ljust(7) + "\n")
        f.write("NOTA 2:".ljust(7) + "\n")
        f.write("NOTA 3:".ljust(7) + "\n")
        f.write("NOTA 4:".ljust(7) + "\n")
        f.write("FACTURAAFECTADA:      " + self['invoice_affected'] + "\n")

        f.close()
        file_destination = 'C:/FACTURAS/' + self['file_name']
        shutil.move(filename,  file_destination)


