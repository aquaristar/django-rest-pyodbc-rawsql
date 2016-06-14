from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

def get_connection():
    import pyodbc
    connection = pyodbc.connect("DSN=abcds;UID=sa;PWD=ksiksi")
    return connection



class Da1YahooHeaderManager(models.Manager):
    def create_yahooh(self, yahooh_data):
        yahooh_sql = """
            INSERT INTO [abcapidb].[dbo].[DA1_YAHOO_HEADER]
            (      
                   ID
                  ,DATESTAMP
                  ,BILL_FULL
                  ,BILL_FIRST
                  ,BILL_LAST
                  ,BILL_ADDRESS_1
                  ,BILL_ADDRESS_2
                  ,BILL_CITY
                  ,BILL_STATE
                  ,BILL_ZIP
                  ,BILL_COUNTRY
                  ,BILL_PHONE
                  ,BILL_EMAIL
                  ,CARD_NAME
                  ,CARD_NUMBER
                  ,CARD_EXPIRY
                  ,TAX_CHARGE
                  ,SHIPPING_CHARGE
                  ,TOTAL
                  ,BILL_CVS
                  ,IP
                  ,GIFT_CARD
                  ,GIFT_AMT_USED
                  ,AUTH
                  ,HOME_DELIVERY
            )
            VALUES (
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s'
            )
        """ % ( 
            yahooh_data['yahooh_id'], 
            yahooh_data['datestamp'], 
            yahooh_data['bill_full'], 
            yahooh_data['bill_first'], 
            yahooh_data['bill_last'], 
            yahooh_data['bill_address_1'], 
            yahooh_data['bill_address_2'], 
            yahooh_data['bill_city'], 
            yahooh_data['bill_state'], 
            yahooh_data['bill_zip'], 
            yahooh_data['bill_country'], 
            yahooh_data['bill_phone'], 
            yahooh_data['bill_email'], 
            yahooh_data['card_name'], 
            yahooh_data['card_number'], 
            yahooh_data['card_expiry'], 
            yahooh_data['tax_charge'], 
            yahooh_data['shipping_charge'], 
            yahooh_data['total'],
            yahooh_data['bill_cvs'], 
            yahooh_data['ip'], 
            yahooh_data['gift_card'], 
            yahooh_data['gift_amt_used'], 
            yahooh_data['auth'], 
            yahooh_data['home_delivery']
            )
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(yahooh_sql)
        connection.commit()

class Da1YahooHeader(models.Model):
    yahooh_id       = models.CharField(db_column='ID',          max_length=20 ,primary_key=True)
    datestamp       = models.CharField(db_column='DATESTAMP',   max_length=28, blank=True, null=True)
    bill_full       = models.CharField(db_column='BILL_FULL',   max_length=50, blank=True, null=True)
    bill_first      = models.CharField(db_column='BILL_FIRST',  max_length=50, blank=True, null=True)
    bill_last       = models.CharField(db_column='BILL_LAST',   max_length=50, blank=True, null=True)
    bill_address_1  = models.CharField(db_column='BILL_ADDRESS_1', max_length=50, blank=True, null=True)
    bill_address_2  = models.CharField(db_column='BILL_ADDRESS_2', max_length=50, blank=True, null=True)
    bill_city       = models.CharField(db_column='BILL_CITY',   max_length=30, blank=True, null=True)
    bill_state      = models.CharField(db_column='BILL_STATE',  max_length=3, blank=True, null=True)
    bill_zip        = models.CharField(db_column='BILL_ZIP',    max_length=10, blank=True, null=True)
    bill_country    = models.CharField(db_column='BILL_COUNTRY',    max_length=30, blank=True, null=True)
    bill_phone      = models.CharField(db_column='BILL_PHONE',  max_length=20, blank=True, null=True)
    bill_email      = models.CharField(db_column='BILL_EMAIL',  max_length=100, blank=True, null=True)
    card_name       = models.CharField(db_column='CARD_NAME',   max_length=50, blank=True, null=True)
    card_number     = models.CharField(db_column='CARD_NUMBER', max_length=24, blank=True, null=True)
    card_expiry     = models.CharField(db_column='CARD_EXPIRY', max_length=10, blank=True, null=True)
    tax_charge      = models.DecimalField(db_column='TAX_CHARGE',   max_digits=10, decimal_places=2)
    shipping_charge = models.DecimalField(db_column='SHIPPING_CHARGE', max_digits=10, decimal_places=2)
    total           = models.DecimalField(db_column='TOTAL',    max_digits=10, decimal_places=2)
    bill_cvs        = models.CharField(db_column='BILL_CVS',    max_length=4, blank=True, null=True)
    ip              = models.CharField(db_column='IP',          max_length=16, blank=True, null=True)
    gift_card       = models.CharField(db_column='GIFT_CARD',   max_length=15, blank=True, null=True)
    gift_amt_used   = models.DecimalField(db_column='GIFT_AMT_USED', max_digits=10, decimal_places=2)
    auth            = models.CharField(db_column='AUTH',        max_length=6, blank=True, null=True)
    home_delivery   = models.DecimalField(db_column='HOME_DELIVERY', max_digits=10, decimal_places=2)

    objects = Da1YahooHeaderManager()





class Da1YahooShiptoManager(models.Manager):
    def create_yahoos(self, yahoos_data):
        yahoos_sql = """
            INSERT INTO [abcapidb].[dbo].[DA1_YAHOO_SHIPTO]
            (      
                   ID
                  ,SHIP_FULL
                  ,SHIP_FIRST
                  ,SHIP_LAST
                  ,SHIP_ADDRESS_1
                  ,SHIP_ADDRESS_2
                  ,SHIP_CITY
                  ,SHIP_STATE
                  ,SHIP_ZIP
                  ,SHIP_COUNTRY
                  ,SHIP_PHONE
                  ,SHIP_EMAIL
                  ,SHIPPING
                  ,COMMENTS
            )
            VALUES (
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s'
            )
        """ % ( 
            yahoos_data['yahoos_id'], 
            yahoos_data['ship_full'], 
            yahoos_data['ship_first'], 
            yahoos_data['ship_last'], 
            yahoos_data['ship_address_1'], 
            yahoos_data['ship_address_2'], 
            yahoos_data['ship_city'], 
            yahoos_data['ship_state'], 
            yahoos_data['ship_zip'], 
            yahoos_data['ship_country'], 
            yahoos_data['ship_phone'], 
            yahoos_data['ship_email'], 
            yahoos_data['shipping'],
            yahoos_data['comments']            
            )
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(yahoos_sql)
        connection.commit()

class Da1YahooShipto(models.Model):
    yahoos_id       = models.CharField(db_column='ID',          max_length=20, primary_key=True)
    ship_full       = models.CharField(db_column='SHIP_FULL',   max_length=50, blank=True, null=True)
    ship_first      = models.CharField(db_column='SHIP_FIRST',  max_length=50, blank=True, null=True)
    ship_last       = models.CharField(db_column='SHIP_LAST',   max_length=50, blank=True, null=True)
    ship_address_1  = models.CharField(db_column='SHIP_ADDRESS_1', max_length=50, blank=True, null=True)
    ship_address_2  = models.CharField(db_column='SHIP_ADDRESS_2', max_length=50, blank=True, null=True)
    ship_city       = models.CharField(db_column='SHIP_CITY',   max_length=30,  blank=True, null=True)
    ship_state      = models.CharField(db_column='SHIP_STATE',  max_length=3,   blank=True, null=True)
    ship_zip        = models.CharField(db_column='SHIP_ZIP',    max_length=10,  blank=True, null=True)
    ship_country    = models.CharField(db_column='SHIP_COUNTRY', max_length=30, blank=True, null=True)
    ship_phone      = models.CharField(db_column='SHIP_PHONE',  max_length=20,  blank=True, null=True)
    ship_email      = models.CharField(db_column='SHIP_EMAIL',  max_length=100, blank=True, null=True)
    shipping        = models.CharField(db_column='SHIPPING',    max_length=50,  blank=True, null=True)
    comments        = models.CharField(db_column='COMMENTS',    max_length=252, blank=True, null=True)

    objects = Da1YahooShiptoManager()




class Da1YahooDetailManager(models.Manager):
    def create_yahood(self, yahood_data):
        yahood_sql = """
            INSERT INTO [abcapidb].[dbo].[DA1_YAHOO_DETAIL]
            (      
                   ID
                  ,ITEM_LINE
                  ,PKG_CNTR
                  ,ITEM_ID
                  ,ITEM_CODE
                  ,ITEM_QUANTITY
                  ,ITEM_UNIT_PRICE
                  ,ITEM_DESCRIPTION
                  ,ITEM_URL
                  ,PICKUP_BRANCH
                  ,PICKUP_DROP
            )
            VALUES (
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
                '%s'
            )
        """ % ( 
            yahood_data['yahood_id'], 
            yahood_data['item_line'], 
            yahood_data['pkg_cntr'], 
            yahood_data['item_id'], 
            yahood_data['item_code'], 
            yahood_data['item_quantity'], 
            yahood_data['item_unit_price'], 
            yahood_data['item_description'], 
            yahood_data['item_url'], 
            yahood_data['pickup_branch'], 
            yahood_data['pickup_drop']      
            )
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(yahood_sql)
        connection.commit()

class Da1YahooDetail(models.Model):
    yahood_id        = models.CharField(    db_column='ID',                 max_length=20, primary_key=True)
    item_line        = models.DecimalField( db_column='ITEM_LINE',          max_digits=8,  primary_key=True, decimal_places=0)
    pkg_cntr         = models.CharField(    db_column='PKG_CNTR',           max_length=2,  primary_key=True)
    item_id          = models.CharField(    db_column='ITEM_ID',            max_length=20,  blank=True, null=True)
    item_code        = models.CharField(    db_column='ITEM_CODE',          max_length=252, blank=True, null=True)
    item_quantity    = models.DecimalField( db_column='ITEM_QUANTITY',      max_digits=8,   decimal_places=0)
    item_unit_price  = models.DecimalField( db_column='ITEM_UNIT_PRICE',    max_digits=10,  decimal_places=2)
    item_description = models.CharField(    db_column='ITEM_DESCRIPTION',   max_length=252, blank=True, null=True)
    item_url         = models.CharField(    db_column='ITEM_URL',           max_length=252, blank=True, null=True)
    pickup_branch    = models.CharField(    db_column='PICKUP_BRANCH',      max_length=4,   blank=True, null=True)
    pickup_drop      = models.CharField(    db_column='PICKUP_DROP',        max_length=1,   blank=True, null=True)

    objects = Da1YahooDetailManager()





class DskGiftMainManager(models.Manager):
    def get_gift(self, accountNum=None, scratchNum=None):
        gift_sql = """
            SELECT KEY_ACCT_NUMBER, 
                ACCT_NUMBER, 
                SOLD_AT_BRANCH, 
                TRAN_DATE_SOLD, 
                TRAN_NO_SOLD, 
                TRAN_TYPE_SOLD, 
                VOID_FLAG, 
                VOID_EMPL_NO, 
                VOID_DATE, 
                EXPIR_DATE, 
                CID_NUMBER, 
                COMP_FLAG, 
                GIFT_AMT, 
                GIFT_AMT_USED
            FROM [abcapidb].[dbo].[DSK_GIFT_MAIN]
            WHERE 1=1            
        """
        if accountNum:
          gift_sql = gift_sql + "AND ACCT_NUMBER LIKE '%s'" % accountNum
        if scratchNum:
          gift_sql = gift_sql + "AND CID_NUMBER LIKE '%s'" % scratchNum

        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(gift_sql)
        result_list = []
        for row in cursor.fetchall():
            p = DskGiftMain(
                    key_acct_number=row[0], 
                    acct_number=row[1], 
                    sold_at_branch=row[2], 
                    tran_date_sold=row[3], 
                    tran_no_sold=row[4], 
                    tran_type_sold=row[5], 
                    void_flag=row[6], 
                    void_empl_no=row[7], 
                    void_date=row[8], 
                    expir_date=row[9], 
                    cid_number=row[10], 
                    comp_flag=row[11], 
                    gift_amt=row[12], 
                    gift_amt_used=row[13]
                )
            result_list.append(p)
        return result_list

class DskGiftMain(models.Model):
    key_acct_number = models.CharField(db_column='KEY_ACCT_NUMBER', max_length=15, primary_key=True)
    acct_number     = models.CharField(db_column='ACCT_NUMBER',     max_length=15, blank=True, null=True)
    sold_at_branch  = models.CharField(db_column='SOLD_AT_BRANCH',  max_length=4, blank=True, null=True)
    tran_date_sold  = models.CharField(db_column='TRAN_DATE_SOLD',  max_length=8, blank=True, null=True)
    tran_no_sold    = models.CharField(db_column='TRAN_NO_SOLD',    max_length=6, blank=True, null=True)
    tran_type_sold  = models.CharField(db_column='TRAN_TYPE_SOLD',  max_length=2, blank=True, null=True)
    void_flag       = models.CharField(db_column='VOID_FLAG',       max_length=1, blank=True, null=True)
    void_empl_no    = models.CharField(db_column='VOID_EMPL_NO',    max_length=5, blank=True, null=True)
    void_date       = models.CharField(db_column='VOID_DATE',       max_length=8, blank=True, null=True)
    expir_date      = models.CharField(db_column='EXPIR_DATE',      max_length=6, blank=True, null=True)
    cid_number      = models.CharField(db_column='CID_NUMBER',      max_length=3, blank=True, null=True)
    comp_flag       = models.CharField(db_column='COMP_FLAG',       max_length=1, blank=True, null=True)
    gift_amt        = models.FloatField(db_column='GIFT_AMT')
    gift_amt_used   = models.FloatField(db_column='GIFT_AMT_USED')

    objects = DskGiftMainManager()





class Da7InventoryStoreManager(models.Manager):
    def get_inventory(self, productId):
        inventory_sql = """
            SELECT KEY_ITEM_NUMBER
              ,KEY_BRANCH
              ,ITEM_NUMBER
              ,BRANCH
              ,REGION
              ,DATE_OF_LAST_SALE
              ,DATE_LAST_RECEIVED
              ,DATE_LAST_PHYSICAL
              ,QTY_LAST_PHY_CNT
              ,DEV_LST_PHY_CNT
              ,MTD_SALES
              ,MTD_COGS
              ,MTD_SALES_1
              ,MTD_COGS_1
              ,MIN_REORDER
              ,QTY_ON_HAND
              ,QTY_ON_ORDER
              ,QTY_COMMITTED
              ,FLOOR_QTY
              ,MTD_UNITS
              ,MTD_UNITS_1
              ,MTD_UNITS_2
              ,MTD_UNITS_3
              ,MTD_UNITS_4
              ,MTD_UNITS_5
              ,MTD_UNITS_6
              ,MTD_UNITS_7
              ,MTD_UNITS_8
              ,MTD_UNITS_9
              ,MTD_UNITS_10
              ,MTD_UNITS_11
              ,MTD_UNITS_12
            FROM [abcapidb].[dbo].[DA7_INVENTORY_STORE]
            WHERE 1=1
        """
        if productId:
          inventory_sql = inventory_sql + "AND KEY_ITEM_NUMBER LIKE '%s'" % productId
        
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(inventory_sql)
        result_list = []
        for row in cursor.fetchall():
            p = Da7InventoryStore(
                    key_item_number=row[0], 
                    key_branch=row[1], 
                    item_number=row[2], 
                    branch=row[3], 
                    region=row[4], 
                    date_of_last_sale=row[5], 
                    date_last_received=row[6], 
                    date_last_physical=row[7], 
                    qty_last_phy_cnt=row[8], 
                    dev_lst_phy_cnt=row[9], 
                    mtd_sales=row[10], 
                    mtd_cogs=row[11], 
                    mtd_sales_1=row[12], 
                    mtd_cogs_1=row[13],
                    min_reorder=row[14], 
                    qty_on_hand=row[15], 
                    qty_on_order=row[16], 
                    qty_committed=row[17], 
                    floor_qty=row[18], 
                    mtd_units=row[19], 
                    mtd_units_1=row[20], 
                    mtd_units_2=row[21], 
                    mtd_units_3=row[22], 
                    mtd_units_4=row[23], 
                    mtd_units_5=row[24], 
                    mtd_units_6=row[25], 
                    mtd_units_7=row[26], 
                    mtd_units_8=row[27], 
                    mtd_units_9=row[28], 
                    mtd_units_10=row[29], 
                    mtd_units_11=row[30], 
                    mtd_units_12=row[31],
                )
            result_list.append(p)
        return result_list

class Da7InventoryStore(models.Model):
    key_item_number     = models.CharField(db_column='KEY_ITEM_NUMBER', max_length=12,  primary_key=True,)
    key_branch          = models.CharField(db_column='KEY_BRANCH',      max_length=4,   primary_key=True,)
    item_number         = models.CharField(db_column='ITEM_NUMBER',     max_length=12,  blank=True, null=True)
    branch              = models.CharField(db_column='BRANCH',          max_length=4,   blank=True, null=True)
    region              = models.CharField(db_column='REGION',          max_length=2,   blank=True, null=True)
    date_of_last_sale   = models.DecimalField(db_column='DATE_OF_LAST_SALE',    max_digits=8, decimal_places=0)
    date_last_received  = models.DecimalField(db_column='DATE_LAST_RECEIVED',   max_digits=8, decimal_places=0)
    date_last_physical  = models.DecimalField(db_column='DATE_LAST_PHYSICAL',   max_digits=8, decimal_places=0)
    qty_last_phy_cnt    = models.DecimalField(db_column='QTY_LAST_PHY_CNT',     max_digits=6, decimal_places=0)
    dev_lst_phy_cnt     = models.DecimalField(db_column='DEV_LST_PHY_CNT',      max_digits=4, decimal_places=0)
    mtd_sales           = models.DecimalField(db_column='MTD_SALES',            max_digits=10, decimal_places=2)
    mtd_cogs            = models.DecimalField(db_column='MTD_COGS',             max_digits=10, decimal_places=0)
    mtd_sales_1         = models.DecimalField(db_column='MTD_SALES_1',          max_digits=8, decimal_places=0)
    mtd_cogs_1          = models.DecimalField(db_column='MTD_COGS_1',           max_digits=8, decimal_places=0)
    min_reorder         = models.DecimalField(db_column='MIN_REORDER',          max_digits=6, decimal_places=0)
    qty_on_hand         = models.DecimalField(db_column='QTY_ON_HAND',          max_digits=6, decimal_places=0)
    qty_on_order        = models.DecimalField(db_column='QTY_ON_ORDER',         max_digits=6, decimal_places=0)
    qty_committed       = models.DecimalField(db_column='QTY_COMMITTED',        max_digits=6, decimal_places=0)
    floor_qty           = models.DecimalField(db_column='FLOOR_QTY',            max_digits=4, decimal_places=0)
    mtd_units           = models.DecimalField(db_column='MTD_UNITS',            max_digits=6, decimal_places=0)
    mtd_units_1         = models.DecimalField(db_column='MTD_UNITS_1',          max_digits=6, decimal_places=0)
    mtd_units_2         = models.DecimalField(db_column='MTD_UNITS_2',          max_digits=6, decimal_places=0)
    mtd_units_3         = models.DecimalField(db_column='MTD_UNITS_3',          max_digits=6, decimal_places=0)
    mtd_units_4         = models.DecimalField(db_column='MTD_UNITS_4',          max_digits=6, decimal_places=0)
    mtd_units_5         = models.DecimalField(db_column='MTD_UNITS_5',          max_digits=6, decimal_places=0)
    mtd_units_6         = models.DecimalField(db_column='MTD_UNITS_6',          max_digits=6, decimal_places=0)
    mtd_units_7         = models.DecimalField(db_column='MTD_UNITS_7',          max_digits=6, decimal_places=0)
    mtd_units_8         = models.DecimalField(db_column='MTD_UNITS_8',          max_digits=6, decimal_places=0)
    mtd_units_9         = models.DecimalField(db_column='MTD_UNITS_9',          max_digits=6, decimal_places=0)
    mtd_units_10        = models.DecimalField(db_column='MTD_UNITS_10',         max_digits=6, decimal_places=0)
    mtd_units_11        = models.DecimalField(db_column='MTD_UNITS_11',         max_digits=6, decimal_places=0)
    mtd_units_12        = models.DecimalField(db_column='MTD_UNITS_12',         max_digits=6, decimal_places=0)

    objects = Da7InventoryStoreManager()