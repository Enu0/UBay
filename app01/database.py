import psycopg2


class PgSql:
    def __init__(self):
        self.conn = psycopg2.connect(host='127.0.0.1', port=5432, user='postgres', password='123456',
                                database='secondhand')
        self.cur = self.conn.cursor()
        
        sql = f"SELECT * FROM idcounter"
        self.cur.execute(sql)
        cur_id = self.cur.fetchall()
        if not cur_id:
            self.initializeProductID()
        self.relations = ['Product']

    def open(self):
        self.conn = psycopg2.connect(host='127.0.0.1', port=5432, user='postgres', password='123456',
                                database='secondhand')
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.commit()
        self.conn.close()

    def getProductID(self):
        self.open()
        
        sql = f"SELECT * FROM idcounter"
        self.cur.execute(sql)
        cur_id = self.cur.fetchall()
        print("balabala")
        print(cur_id)
        self.close()
        return cur_id[0][0]

    def updateNextProductID(self, cur_id):
        self.open()
        sql = f"UPDATE idcounter SET cur_id = cur_id+1 WHERE cur_id={cur_id}"
        self.cur.execute(sql)
        self.close()

    def initializeProductID(self):
        self.open()
        sql = f"INSERT INTO idcounter values({0})"
        self.cur.execute(sql)
        self.close()

    def addProduct(self, name, p_type, p_id, images, seller):
        self.open()
        sql = f"INSERT INTO product values('{name}', '{p_type}', {p_id}, '{images}', '{seller}');"
        self.cur.execute(sql)
        self.close()

    def addProductInfo(self, p_id, price, description):
        self.open()
        sql = f"INSERT INTO productinfo values({p_id}, {price}, '{description}');"
        self.cur.execute(sql)
        self.close()

    def loadProductInfo(self):
        self.open()
        sql = f"SELECT p_name, p_type, image_path, seller, price, description FROM product,productinfo WHERE product.p_id = productinfo.p_id"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        self.close()
        return rows



