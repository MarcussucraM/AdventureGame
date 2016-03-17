'''
This class contains all the layouts for levels, to build a level follow the
character mapping rules:

x = wall
s = start location
k = key
d = door
m = movable block
u = 1up
l = lava
h = horizontal bounce monster
v = vertical bounce monster

Make sure your levels have atleast one key and a door, otherwise you can't get
out of the level
'''


class Levels(object):
    def __init__(self):
        self.layouts =[None]*10
        self.layouts[0] = ["xxxxxxxxxx",
                           "x..m.mx..x",
                           "x...m.m..x",
                           "x..m.mm..x",
                           "xs..m.x..d",
                           "x..m.x...x",
                           "x...mkx..x",
                           "x..m.mx..x",
                           "xxxxxxxxxx"]
                      
        self.layouts[1] = ["xxxxxxxxxx",
                           "xxxxxx...x",
                           "x..m.ml..x",
                           "xs...ml..x",
                           "x....ml..x",
                           "xxxxxxx.xx",
                           "x...dxxlxx",
                           "x..xx.m.xx",
                           "x..l.m.mkx",
                           "x..l....xx",
                           "xxxxxxxxxx"]
                           
        self.layouts[2] = ["xxxxxxxxxxxxxxxx",
                           "x..vvvv..vvvv..x",
                           "x.......k......x",
                           "xh............hx",
                           "x..............x",
                           "x..............x",
                           "xh............hx",
                           "xh............hx",
                           "xh............hx",
                           "xh............hx",
                           "x..............x",
                           "xs.............d",
                           "x..............x",
                           "xh............hx",
                           "xh............hx",
                           "xh............hx",
                           "xh..........u.hx",
                           "x..............x",                          
                           "x..............x",
                           "x..vvvv..vvvv..x",
                           "xxxxxxxxxxxxxxxx"]
               
                      
        self.layouts[3] = ["xxxxxxxxxxxxxxxxxxxxxxxxxxx",
                           "xxxxxxxxxxxxxxxxxxxxxxxxxxx",
                           "xlllllllllll.s.lllllllllllx",
                           "xllllllllll.....lllllllll.d",
                           "xlllllllll.......llllllll.x",
                           "xllllllll.........lllllll.x",
                           "xhllllll...........llllllhx",
                           "x.llllll............lllllux",
                           "xhllll...............llllhx",
                           "xhlll.................lllhx",
                           "xhll...................llhx",
                           "xh.......................hx",
                           "xh.......................hx",
                           "xh.......................hx",
                           "x.ll...................ll.x",
                           "x.lll........k........lll.x",
                           "xhllll...............llllhx",
                           "xllllll.............lllll.x",
                           "xlllllll...........llllll.x",
                           "xllllllll.........lllllll.x",
                           "xlllllllll.......llllllll.x",
                           "xllllllllll.....lllllllll.x",
                           "xlllllllllll.l.llllllllll.x",
                           "xlllllllllll..............x",
                           "xxxxxxxxxxxxxxxxxxxxxxxxxxx"]
                           
        self.layouts[4] = ["xxxxxxxxxxxxxx",
                           "xsx.mx......xx",
                           "x.x.mlmmxx..xx",
                           "x.x.xx.lxx..xx",
                           "x.x..m.mxx..xx",
                           "xmx.mmx.xx..xx",
                           "x.xm..x.xx..ux",
                           "x.x.ml..xx..xx",
                           "x.xx.xxxxx..xx",
                           "x.xx.xxlkx..xx",
                           "x..m....xu..xx",
                           "x.xx.xx.xx..xx",
                           "xxxx.xx.xx..xx",
                           "xxxx.xx.xx..xx",
                           "xxxx....xxvvxx",
                           "xxxxxxxxxxxdxx"]
                           

        self.layouts[5] = ["xxxxxxxxxxxxxxx",
                           "xxxxxxxxxxx..xx",
                           "xxk..........xx",
                           "xx..xxxxxxxxmxx",
                           "xx..llm...mx.xx",
                           "xlllxxxm.m.x.xx",
                           "xs......m..x.xx",
                           "x...xxxmmm.x.xx",
                           "xxxlxxx....xlxx",
                           "xxx.xxx.xxxxlxx",
                           "xxx.x..xxxxx..x",
                           "x..mxml.m...x.x",
                           "x.l..m..xmm.x.x",
                           "xx.lxl......x.x",
                           "xxxxxxxxxxxxxdx"]
                           
                           
        self.layouts[6] = ["xxxxxxxxxxxxxxxxxxxxxxx",
                           "x....l.......l...lv..hx",
                           "x....l.......l..ul...hx",
                           "x....l.......l..kl....x",
                           "x....l...l...l...l....x",
                           "xs.m.l...l...l...l....d",
                           "x....l...l...l...l....x",
                           "x....l...l...l...l....x",
                           "x....l...l...l...l....x",
                           "x....l...l...l...l....x",
                           "x....l...l...l...l....x",
                           "x........l...l...l....x",
                           "x........l...l...l...hx",
                           "x........l.......lv..hx",
                           "xxxxxxxxxxxxxxxxxxxxxxx"]
                           
        self.layouts[7] = ["xxxxxxxxxxxxxxx",
                           "xk............x",
                           "x......v......x",
                           "xxx...v.v.....x",
                           "x.x..v...v....x",
                           "x.x.v.....v...x",
                           "xsxv.......v..d",
                           "x.............x",
                           "xxxxxxxxxxxxxxx"]
                           
        self.layouts[8] = ["xxxxxxxxxxxxxxxxxxx",
                           "xulllll........xxkx",
                           "xllxlll......m.x..x",
                           "xl.m.xx...x.m.m.m.x",
                           "x.x.x.xvvx.m.m.m.mx",
                           "x.x...xxx.m.m.m.m.x",
                           "x.x.x.xxsx.x.x.x.xx",
                           "xllmm.x..lllllllllx",
                           "xdx.x.xmll.....h..x",
                           "xxx.x.x.ll......hux",
                           "xx....m.m........hx",
                           "xxxxxxx.x.........x",
                           "xxxxxxxxxxxxxxxxxxx"]
        
        #final level
        self.layouts[9] = [""]
                           
                           

                           
        