from django.contrib.auth.models import User, Group
from abcapi.models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')




class Da1YahooHeaderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Da1YahooHeader
		fields = ('yahooh_id', 'datestamp', 'bill_full', 'bill_first', 'bill_last', 'bill_address_1', 'bill_address_2', 'bill_city', 'bill_state', 'bill_zip', 'bill_country', 'bill_phone',
		'bill_email', 'card_name', 'card_number', 'card_expiry', 'tax_charge', 'shipping_charge', 'total', 'bill_city', 'ip', 'gift_card', 'gift_amt_used', 'auth', 'home_delivery')

class Da1YahooShiptoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Da1YahooShipto
		fields = ('yahoos_id', 'ship_full', 'ship_first', 'ship_last', 'ship_address_1', 'ship_address_2', 'ship_city', 'ship_state', 'ship_zip', 'ship_country', 'ship_phone', 'ship_email', 'shipping', 'comments')

class Da1YahooDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Da1YahooDetail
		fields = ('yahood_id', 'item_line', 'pkg_cntr', 'item_id', 'item_code', 'item_quantity', 'item_unit_price', 'item_description', 'item_url', 'pickup_branch', 'pickup_drop')




class DskGiftMainSerializer(serializers.ModelSerializer):
	class Meta:
		model = DskGiftMain
		fields = ('key_acct_number', 'acct_number', 'sold_at_branch', 'tran_date_sold', 'tran_no_sold', 'tran_type_sold', 'void_flag', 'void_empl_no', 'void_date', 'expir_date', 'cid_number', 'comp_flag', 'gift_amt', 'gift_amt_used')




class Da7InventoryStoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Da7InventoryStore
		fields = ('key_item_number', 'key_branch', 'item_number', 'branch', 'region', 'date_of_last_sale', 'date_last_received', 'date_last_physical', 'qty_last_phy_cnt', 'dev_lst_phy_cnt', 'mtd_sales', 'mtd_cogs', 'mtd_sales_1', 'mtd_cogs_1', 'min_reorder', 'qty_on_hand', 'qty_on_order', 'qty_committed', 'floor_qty', 'mtd_units', 'mtd_units_1', 'mtd_units_2', 'mtd_units_3', 'mtd_units_4', 'mtd_units_5', 'mtd_units_6', 'mtd_units_7', 'mtd_units_8', 'mtd_units_9', 'mtd_units_10', 'mtd_units_11', 'mtd_units_12' )




class OrderSerializer(serializers.Serializer):	
	yahooh = Da1YahooHeaderSerializer(read_only=False)
	yahoos = Da1YahooShiptoSerializer(read_only=False)
	yahood = Da1YahooDetailSerializer(many = True, read_only=False)

	pass