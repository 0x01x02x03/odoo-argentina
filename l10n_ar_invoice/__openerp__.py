# -*- coding: utf-8 -*-
{'active': False,
 'author': 'OpenERP - Team de Localizaci\xc3\xb3n Argentina',
 'category': 'Localization/Argentina',
 'depends': [
     'account',
     'l10n_ar_base',
     'l10n_ar_base_vat',
 ],
 'description': """
Facturación y Documentos AFIP - Argentina
=========================================
""",
 'init_xml': [],
 'installable': True,
 'license': 'AGPL-3',
 'name': 'Facturación y Documentos AFIP - Argentina',
 'demo': [
     # 'demo/partner_demo.xml',
     # 'demo/res.company.csv',
     # 'demo/afip.point_of_sale.csv',
     # 'demo/account.account.csv',
     # 'demo/account.journal.csv',
     # 'demo/account.invoice.csv',
     # 'demo/account.invoice.line.csv',
    ],
 'test': [
          # test cases should be re-writed
          # 'test/products.yml',
          # 'test/partners.yml',
          # 'test/com_ri1.yml',
          # 'test/com_ri2.yml',
          # 'test/com_rm1.yml',
          # 'test/inv_ri2ri.yml',
          # 'test/inv_rm2ri.yml',
          # 'test/inv_ri2rm.yml',
          # 'test/bug_1042944.yml'
          ],
 'data': [
     'security/l10n_ar_invoice_security.xml',
     'data/responsability.xml',
     'data/afip.document_letter.csv',
     'data/afip.document_class.csv',
     'data/document_type.xml',
     'data/partner.xml',
     'data/country.xml',
     'data/res.currency.csv',
     'data/afip.concept_type.csv',
     # 'data/decimal_precision_data.xml', probando si no es necesario
     'view/partner_view.xml',
     'view/company_view.xml',
     'view/country_view.xml',
     'view/afip_menuitem.xml',
     'view/afip_document_letter_view.xml',
     'view/afip_concept_type_view.xml',
     'view/afip_optional_type_view.xml',
     'view/afip_document_type_view.xml',
     'view/afip_responsability_view.xml',
     'view/afip_document_class_view.xml',
     'view/afip_point_of_sale_view.xml',
     'view/account_journal_afip_document_class_view.xml',
     'view/account_tax_code_view.xml',
     'view/journal_view.xml',
     'view/invoice_view.xml',
     'view/account_move_view.xml',
     'view/account_move_line_view.xml',
     'view/currency_view.xml',
     'wizard/config_view.xml',
     'invoice_template.xml',
     'security/ir.model.access.csv',
     'security/l10n_ar_invoice_security.xml',
 ],
 'version': '2.7.243',
 }
