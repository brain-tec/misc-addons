.. image:: https://itpp.dev/images/infinity-readme.png
   :alt: Tested and maintained by IT Projects Labs
   :target: https://itpp.dev

=======================
 S3 Attachment Storage
=======================

* The module allows to upload the attachments in Amazon S3 automatically without storing them in Odoo database. It will allow to reduce the load on your server. Attachments will be uploaded on S3 depending on the condition you specified in Odoo settings. So you can choose and manage which type of attachments should be uploaded on S3.
* It is useful in cases where your database was crashed, because you will be able to easily restore all attachments from external storage at any time.
* The possibility to use one external storage for any number of databases.

Questions?
==========

To get an assistance on this module contact us by email :arrow_right: help@itpp.dev

Contributors
============
* Ildar Nasyrov <iledarn@it-projects.info>

Further information
===================

Odoo Apps Store: https://apps.odoo.com/apps/modules/10.0/ir_attachment_s3/


Tested on `Odoo 10.0 <https://github.com/odoo/odoo/commit/f05e8655ee4ee7205c67006ca5a8cb30ed445c81>`_
