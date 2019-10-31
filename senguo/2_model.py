class Calculate:
    def __init__(self):
        '''
        读取数据库，确定stock，cost，sales的初始值
        '''
        self.stock=0
        self.cost=0
        self.sales=0

    def purchase(self,id,quantity,price):
        '''
        采购过程处理
        id:str类型
        quantity:float类型，为每次采购的数量
        price：float类型，为采购单价
        '''
        self.stock+=quantity
        self.cost+=quantity*price
        # 将该条数据插入采购表中
        # 更新库存，利润表

    def sell(self,id,quantity,price):
        ''' 销售过程处理，支持退货操作
        id:str类型
        quantity:float类型，为每次售卖数量
        price:float类型，为售卖单价
        '''
        if self.stock<quantity:
            print('不能超卖')
        else:
            self.sales+=quantity*price
        # 将该条数据插入销售表中
        # 更新库存，利润表
    
    def profit(self):
        # 返回值：float类型，总利润
        return self.sales-self.cost


