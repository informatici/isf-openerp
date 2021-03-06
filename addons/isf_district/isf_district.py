from openerp.osv import osv
from openerp.osv import fields
from openerp.tools.translate import _
import time

class isf_district_district(osv.osv):
	""" District """
	_name = "isf.district.district"
	_description = "District"
	_columns = {
		'code' : fields.char('District code', size=20, required=True),
		'name' : fields.char('District name', size=100, required=True),
	}
	
	_sql_constraints = [
        	('code', 'unique(code)', 'The code of the district must be unique')
    	]


isf_district_district()

class isf_district_zone(osv.osv):
	""" Zone """
	_name = "isf.district.zone"
	_description = "Zone"
	_columns = {
		'code' : fields.char('Zone code', size=20, required=True),
		'district_ids' : fields.many2one('isf.district.district', 'code'),
		'name' : fields.char('Zone name', size=100, required=True),
	}
	
	_sql_constraints = [
        	('code_zone_uniq', 'unique(code,district_ids)', 'The code of the district must be unique'),
    	]

	
isf_district_zone()

class isf_district_subzone(osv.osv):
		
	""" Sub Zone """
	_name = "isf.district.subzone"
	_description = "Sub Zone"
	
	_columns = {
		'code' : fields.char('Sub Zone code', size=20, required=True),
		'district_ids' : fields.many2one('isf.district.district','code'),
		'zone_ids' : fields.many2one('isf.district.zone','code',domain="[('district_ids', '=', district_ids)]"),
		'name' : fields.char('Sub Zone name', size=100, required=True),
	}
	
	_sql_constraints = [
        	('code_subzone_uniq', 'unique(code,zone_ids,district_ids)', 'The code of the district must be unique'),
    	]


	
isf_district_subzone()

class isf_district_block(osv.osv):
	""" Block """
	_name = "isf.district.block"
	_description = "Block"
	_columns = {
		'name' : fields.char('Block Code', size=4, required=True),
		'subzone_ids' : fields.many2one('isf.district.subzone',"code",domain="[('zone_ids', '=', zone_ids)]"),
		'zone_ids' : fields.many2one('isf.district.zone', "code",domain="[('district_ids', '=', district_ids)]"),
		'district_ids' : fields.many2one('isf.district.district', 'code'), 
	}
	
	_sql_constraints = [
        	('code_block_uniq', 'unique(name,subzone_ids,zone_ids,district_ids)', 'The code of the plot must be unique')
    	]
	
isf_district_block()

class isf_district_plot(osv.osv):
	""" Plot """
	_name = "isf.district.plot"
	_description = "Plot"
	_columns = {
		'name' : fields.char('Plot Code', size=10, required=True),
		'subzone_ids' : fields.many2one('isf.district.subzone',"code",domain="[('zone_ids', '=', zone_ids)]"),
		'zone_ids' : fields.many2one('isf.district.zone', "code",domain="[('district_ids', '=', district_ids)]"),
		'district_ids' : fields.many2one('isf.district.district', 'code'), 
		'block_ids' : fields.many2one('isf.district.block','code',required=True,domain="['&',('district_ids', '=', district_ids),'&',('zone_ids', '=', zone_ids),('subzone_ids', '=', subzone_ids)]"),
		'width' : fields.integer('Width',size=4, Required=False),
		'height' : fields.integer('Height',size=4, Required=False),
		'length' : fields.integer('Length',size=4, Required=False),
		'unit_ids' : fields.many2one('product.uom', 'Unit of Measure',required=False), 
	}
	
	_sql_constraints = [
        	('code_plot_uniq', 'unique(name,block_ids,district_ids,zone_ids,subzone_ids)', 'The code of the plot must be unique')
    	]
	
isf_district_plot()




