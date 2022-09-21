from . import ingeint_utils
import shutil
import os


def create_invoice(self):
    filename = "C:/PROCESANDO/" + self['file_name']
    with open(filename, 'w') as f:
        f.write("FACTURA:         " + self['invoice_number'] + "\n")
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
        f.write("CHEQUES".ljust(24) + str(0.0) + "\n")
        f.write("TARJ / DEBITO:".ljust(24) + str(0.0) + "\n")
        f.write("Tranf en Bs:".ljust(24) + str(0.0) + "\n")
        f.write("Transf en USD:".ljust(24) + str(0.0) + "\n")
        f.write("Transf EURO:".ljust(24) + str(0.0) + "\n")
        f.write("Efect USD:".ljust(24) + str(0.0) + "\n")
        f.write("Efect EURO:".ljust(24) + str(0.0) + "\n")
        f.write("Pago movil:".ljust(24) + str(0.0) + "\n")
        f.write("CREDITO:".ljust(24) + str(0.0) + "\n")
        f.write("NOTA 1:".ljust(7) + "\n")
        f.write("NOTA 2:".ljust(7) + "\n")
        f.write("NOTA 3:".ljust(7) + "\n")
        f.write("NOTA 4:".ljust(7) + "\n")

        f.close()
        file_destination = 'C:/FACTURAS/' + self['file_name']
        shutil.move(filename,  file_destination)


def create_credit_note(self):
    filename = "C:/PROCESANDO/" + self['file_name']
    with open(filename, 'w') as f:
        f.write("DEVOLUCION:      " + self['invoice_number'] + "\n")
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
        f.write("CHEQUES".ljust(24) + str(0.0) + "\n")
        f.write("TARJ / DEBITO:".ljust(24) + str(0.0) + "\n")
        f.write("TARJ / CREDITO:".ljust(24) + str(0.0) + "\n")
        f.write("Tranf en Bs:".ljust(24) + str(0.0) + "\n")
        f.write("Transf en USD:".ljust(24) + str(0.0) + "\n")
        f.write("Transf EURO:".ljust(24) + str(0.0) + "\n")
        f.write("Efect USD:".ljust(24) + str(0.0) + "\n")
        f.write("Efect EURO:".ljust(24) + str(0.0) + "\n")
        f.write("Pago movil:".ljust(24) + str(0.0) + "\n")
        f.write("CREDITO:".ljust(24) + str(0.0) + "\n")
        f.write("NOTA 1:" .ljust(7) + "\n")
        f.write("NOTA 2:".ljust(7) + "\n")
        f.write("NOTA 3:".ljust(7) + "\n")
        f.write("NOTA 4:".ljust(7) + "\n")
        f.write("FACTURAAFECTADA:      " + self['invoice_affected'] + "\n")

        f.close()
        file_destination = 'C:/FACTURAS/' + self['file_name']
        shutil.move(filename,  file_destination)


