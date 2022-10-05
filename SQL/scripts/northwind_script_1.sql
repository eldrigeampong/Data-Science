
/*
 Tables Merged For This Script 
 
select * from customers c;
select * from orders o;
select * from order_details od;
select * from products p;
select * from categories c2;

 */



/* sql script for customers data */


with 
	customers_orders_tbl as (
	                          select 
	                                distinct
	                                         c.customerid,
	                                         c.companyname,
	                                         c.contactname,
	                                         c.contacttitle,
	                                         c.address,
	                                         c.city,
	                                         c.region,
	                                         c.postalcode,
	                                         c.country,
	                                         c.phone,
	                                         c.fax,
	                                         o.orderid,
	                                         o.orderdate,
	                                         o.shippeddate,
	                                         o.shipvia,
	                                         o.freight,
	                                         o.shipcity,
	                                         o.shipcountry,
	                                         od.productid,
	                                         p.productname,
	                                         od.unitprice,
	                                         od.quantity,
	                                         od.discount,
	                                         p.categoryid,
	                                         c2.categoryname,
	                                         c2.description 
	                          from customers c
	                          left join orders o on c.customerid = o.customerid
	                          left join order_details od on o.orderid = od.orderid
	                          left join products p on od.productid = p.productid
	                          left join categories c2 on p.categoryid = c2.categoryid 
	                        )
	                          
select
	*
from
	customers_orders_tbl;









