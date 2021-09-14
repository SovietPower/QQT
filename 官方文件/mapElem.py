# -*- coding: utf-8 -*-
class QQTMapElem:
    version = 5         # verison
    LifeTime = -1      # 地图元素几次被炸毁
    canMove = 0         # can move
    canDoSpecial = 0    # have special event
    offset = (0, 0)     # image offset
    size = (1, 1)       # image area size
    Level = 256
    GridAttr=(0,)#玩家穿越，遮蔽玩家，火焰穿越，遮蔽火焰
    canHide = 0   #顶层元素属性

class QQTMapElem15020(QQTMapElem):
    LifeTime = 1
    offset = (0, 10)
    imageID = 15020
    GridAttr = (0,)

class QQTMapElem15021(QQTMapElem):
    offset = (1, 10)
    imageID = 15021
    GridAttr = (0,)

class QQTMapElem14007(QQTMapElem):
    offset = (-1, 23)
    imageID = 14007
    GridAttr = (0,)

class QQTMapElem14010(QQTMapElem):
    offset = (-5, 9)
    imageID = 14010
    GridAttr = (0,)

class QQTMapElem14012(QQTMapElem):
    offset = (1, 42)
    imageID = 14012
    GridAttr = (0,)

class QQTMapElem17053(QQTMapElem):
    offset = (0, 16)
    imageID = 17053
    GridAttr = (0,)

class QQTMapElem17055(QQTMapElem):
    offset = (5, 10)
    imageID = 17055
    GridAttr = (0,)

class QQTMapElem13007(QQTMapElem):
    LifeTime = 1
    offset = (3, 13)
    imageID = 13007
    GridAttr = (0,)

class QQTMapElem13008(QQTMapElem):
    LifeTime = 1
    offset = (2, 13)
    imageID = 13008
    GridAttr = (0,)

class QQTMapElem17105(QQTMapElem):
    imageID = 17105
    GridAttr = (5397,)
    canHide = 1

class QQTMapElem13010(QQTMapElem):
    LifeTime = 1
    offset = (3, 13)
    imageID = 13010
    GridAttr = (0,)

class QQTMapElem17107(QQTMapElem):
    offset = (0, 1)
    imageID = 17107
    GridAttr = (5397,)
    canHide = 1

class QQTMapElem17108(QQTMapElem):
    imageID = 17108
    GridAttr = (6682,)
    canHide = 1

class QQTMapElem17109(QQTMapElem):
    imageID = 17109
    GridAttr = (5397,)
    canHide = 1

class QQTMapElem17110(QQTMapElem):
    offset = (-2, 0)
    imageID = 17110
    GridAttr = (6682,)
    canHide = 1

class QQTMapElem17112(QQTMapElem):
    imageID = 17112
    GridAttr = (7196,)
    canHide = 1

class QQTMapElem17113(QQTMapElem):
    imageID = 17113
    GridAttr = (6425,)
    canHide = 1

class QQTMapElem17059(QQTMapElem):
    offset = (1, 84)
    size = (3, 2)
    imageID = 17059
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem12008(QQTMapElem):
    canDoSpecial = 1
    offset = (6, 41)
    imageID = 12008
    GridAttr = (7967,)
    canHide = 1

class QQTMapElem16105(QQTMapElem):
    offset = (1, 5)
    imageID = 16105
    GridAttr = (0,)

class QQTMapElem12010(QQTMapElem):
    offset = (4, 25)
    imageID = 12010
    GridAttr = (0,)

class QQTMapElem16107(QQTMapElem):
    offset = (2, 12)
    imageID = 16107
    GridAttr = (0,)

class QQTMapElem12012(QQTMapElem):
    offset = (2, 29)
    imageID = 12012
    GridAttr = (5397,)
    canHide = 1

class QQTMapElem16116(QQTMapElem):
    LifeTime = 1
    offset = (4, 12)
    imageID = 16116
    GridAttr = (0,)

class QQTMapElem17064(QQTMapElem):
    offset = (0, 20)
    imageID = 17064
    GridAttr = (0,)

class QQTMapElem11002(QQTMapElem):
    LifeTime = 1
    offset = (3, 10)
    imageID = 11002
    GridAttr = (0,)

class QQTMapElem11006(QQTMapElem):
    size = (1, 9)
    imageID = 11006
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem13055(QQTMapElem):
    size = (15, 1)
    imageID = 13055
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem13056(QQTMapElem):
    offset = (1, 32)
    size = (2, 1)
    imageID = 13056
    GridAttr = (0, 0)

class QQTMapElem13057(QQTMapElem):
    offset = (4, 23)
    imageID = 13057
    GridAttr = (0,)

class QQTMapElem10004(QQTMapElem):
    imageID = 10004
    GridAttr = (0,)

class QQTMapElem17018(QQTMapElem):
    LifeTime = 1
    offset = (0, 15)
    imageID = 17018
    GridAttr = (0,)

class QQTMapElem17019(QQTMapElem):
    LifeTime = 1
    offset = (-1, 15)
    imageID = 17019
    GridAttr = (0,)

class QQTMapElem17021(QQTMapElem):
    LifeTime = 3
    offset = (0, 16)
    imageID = 17021
    GridAttr = (0,)

class QQTMapElem17022(QQTMapElem):
    LifeTime = 2
    offset = (0, 15)
    imageID = 17022
    GridAttr = (0,)

class QQTMapElem17023(QQTMapElem):
    LifeTime = 1
    offset = (0, 12)
    imageID = 17023
    GridAttr = (0,)

class QQTMapElem17024(QQTMapElem):
    offset = (0, 19)
    imageID = 17024
    GridAttr = (0,)

class QQTMapElem17025(QQTMapElem):
    imageID = 17025
    GridAttr = (3840,)

class QQTMapElem17027(QQTMapElem):
    offset = (1, 24)
    imageID = 17027
    GridAttr = (0,)

class QQTMapElem17028(QQTMapElem):
    offset = (1, 15)
    imageID = 17028
    GridAttr = (0,)

class QQTMapElem4045(QQTMapElem):
    imageID = 4045
    GridAttr = (0,)

class QQTMapElem14103(QQTMapElem):
    offset = (1, 14)
    imageID = 14103
    GridAttr = (0,)

class QQTMapElem17039(QQTMapElem):
    offset = (-3, 16)
    size = (3, 2)
    imageID = 17039
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem10008(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (1, 13)
    imageID = 10008
    GridAttr = (0,)

class QQTMapElem17046(QQTMapElem):
    offset = (0, 10)
    imageID = 17046
    GridAttr = (0,)

class QQTMapElem17047(QQTMapElem):
    offset = (0, 17)
    imageID = 17047
    GridAttr = (0,)

class QQTMapElem17048(QQTMapElem):
    LifeTime = 1
    offset = (0, 17)
    imageID = 17048
    GridAttr = (0,)

class QQTMapElem17050(QQTMapElem):
    offset = (-2, 58)
    size = (2, 1)
    imageID = 17050
    GridAttr = (0, 0)

class QQTMapElem15003(QQTMapElem):
    LifeTime = 1
    offset = (1, 21)
    imageID = 15003
    GridAttr = (0,)

class QQTMapElem15004(QQTMapElem):
    LifeTime = 1
    offset = (2, 20)
    imageID = 15004
    GridAttr = (0,)

class QQTMapElem15005(QQTMapElem):
    offset = (1, 22)
    imageID = 15005
    GridAttr = (0,)

class QQTMapElem17054(QQTMapElem):
    offset = (4, 31)
    imageID = 17054
    GridAttr = (0,)

class QQTMapElem15007(QQTMapElem):
    offset = (4, 12)
    imageID = 15007
    GridAttr = (0,)

class QQTMapElem17056(QQTMapElem):
    offset = (-5, 0)
    imageID = 17056
    GridAttr = (0,)

class QQTMapElem15009(QQTMapElem):
    offset = (4, 12)
    size = (3, 2)
    imageID = 15009
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem15010(QQTMapElem):
    offset = (0, 18)
    imageID = 15010
    GridAttr = (5397,)
    canHide = 1

class QQTMapElem15011(QQTMapElem):
    offset = (0, 1)
    size = (4, 2)
    imageID = 15011
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem15012(QQTMapElem):
    offset = (0, 22)
    imageID = 15012
    GridAttr = (0,)

class QQTMapElem15013(QQTMapElem):
    offset = (0, 7)
    imageID = 15013
    GridAttr = (0,)

class QQTMapElem15014(QQTMapElem):
    LifeTime = 1
    offset = (0, 15)
    imageID = 15014
    GridAttr = (0,)

class QQTMapElem17063(QQTMapElem):
    offset = (2, 15)
    size = (3, 3)
    imageID = 17063
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem15016(QQTMapElem):
    offset = (5, 10)
    imageID = 15016
    GridAttr = (0,)

class QQTMapElem15017(QQTMapElem):
    LifeTime = 1
    offset = (5, 12)
    imageID = 15017
    GridAttr = (0,)

class QQTMapElem15018(QQTMapElem):
    offset = (4, 12)
    imageID = 15018
    GridAttr = (0,)

class QQTMapElem17067(QQTMapElem):
    offset = (-16, 0)
    imageID = 17067
    GridAttr = (0,)

class QQTMapElem17068(QQTMapElem):
    offset = (12, -4)
    imageID = 17068
    GridAttr = (3845,)

class QQTMapElem17069(QQTMapElem):
    offset = (1, 36)
    imageID = 17069
    GridAttr = (0,)

class QQTMapElem17070(QQTMapElem):
    offset = (6, 36)
    imageID = 17070
    GridAttr = (0,)

class QQTMapElem10013(QQTMapElem):
    canDoSpecial = 11
    offset = (-1, 43)
    imageID = 10013
    GridAttr = (0,)

class QQTMapElem17072(QQTMapElem):
    offset = (6, 0)
    size = (1, 3)
    imageID = 17072
    GridAttr = (3845, 3845, 3855)

class QQTMapElem17073(QQTMapElem):
    offset = (0, 20)
    imageID = 17073
    GridAttr = (0,)

class QQTMapElem17074(QQTMapElem):
    offset = (0, -6)
    imageID = 17074
    GridAttr = (0,)

class QQTMapElem17075(QQTMapElem):
    imageID = 17075
    GridAttr = (0,)

class QQTMapElem17076(QQTMapElem):
    offset = (1, 14)
    size = (2, 1)
    imageID = 17076
    GridAttr = (0, 0)

class QQTMapElem17077(QQTMapElem):
    offset = (-2, 19)
    imageID = 17077
    GridAttr = (0,)

class QQTMapElem17078(QQTMapElem):
    offset = (0, 1)
    imageID = 17078
    GridAttr = (0,)

class QQTMapElem17079(QQTMapElem):
    offset = (-31, 0)
    imageID = 17079
    GridAttr = (0,)

class QQTMapElem17080(QQTMapElem):
    offset = (14, -8)
    imageID = 17080
    GridAttr = (0,)

class QQTMapElem17081(QQTMapElem):
    imageID = 17081
    GridAttr = (0,)

class QQTMapElem17082(QQTMapElem):
    offset = (0, 6)
    size = (3, 1)
    imageID = 17082
    GridAttr = (3850, 3850, 3855)

class QQTMapElem17083(QQTMapElem):
    offset = (7, 0)
    size = (1, 3)
    imageID = 17083
    Level = 16777216
    GridAttr = (3845, 3845, 3845)

class QQTMapElem10016(QQTMapElem):
    imageID = 10016
    GridAttr = (0,)

class QQTMapElem14113(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 15)
    imageID = 14113
    GridAttr = (0,)

class QQTMapElem17100(QQTMapElem):
    LifeTime = 1
    offset = (0, 13)
    imageID = 17100
    GridAttr = (0,)

class QQTMapElem17101(QQTMapElem):
    LifeTime = 1
    offset = (0, 13)
    imageID = 17101
    GridAttr = (0,)

class QQTMapElem17102(QQTMapElem):
    LifeTime = 1
    offset = (0, 13)
    imageID = 17102
    GridAttr = (0,)

class QQTMapElem17103(QQTMapElem):
    LifeTime = 1
    offset = (1, 12)
    imageID = 17103
    GridAttr = (0,)

class QQTMapElem17104(QQTMapElem):
    LifeTime = 1
    offset = (0, 17)
    imageID = 17104
    GridAttr = (0,)

class QQTMapElem13009(QQTMapElem):
    LifeTime = 1
    offset = (3, 13)
    imageID = 13009
    GridAttr = (0,)

class QQTMapElem17106(QQTMapElem):
    imageID = 17106
    GridAttr = (6682,)
    canHide = 1

class QQTMapElem13011(QQTMapElem):
    offset = (2, 14)
    imageID = 13011
    GridAttr = (0,)

class QQTMapElem13012(QQTMapElem):
    offset = (4, 19)
    size = (2, 1)
    imageID = 13012
    GridAttr = (0, 0)

class QQTMapElem13013(QQTMapElem):
    offset = (2, 15)
    imageID = 13013
    GridAttr = (0,)

class QQTMapElem13014(QQTMapElem):
    offset = (2, 34)
    imageID = 13014
    GridAttr = (0,)

class QQTMapElem17111(QQTMapElem):
    imageID = 17111
    GridAttr = (5654,)
    canHide = 1

class QQTMapElem13016(QQTMapElem):
    canDoSpecial = 1
    offset = (4, 55)
    size = (2, 1)
    imageID = 13016
    GridAttr = (6682, 6682)
    canHide = 1

class QQTMapElem13017(QQTMapElem):
    canDoSpecial = 2
    offset = (6, 53)
    size = (2, 1)
    imageID = 13017
    GridAttr = (4112, 6682)
    canHide = 1

class QQTMapElem17114(QQTMapElem):
    imageID = 17114
    GridAttr = (5907,)
    canHide = 1

class QQTMapElem17115(QQTMapElem):
    imageID = 17115
    GridAttr = (7967,)
    canHide = 1

class QQTMapElem13020(QQTMapElem):
    size = (3, 13)
    imageID = 13020
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem13021(QQTMapElem):
    offset = (41, 0)
    size = (1, 13)
    imageID = 13021
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem13022(QQTMapElem):
    LifeTime = 1
    canMove = 2
    canDoSpecial = 7
    offset = (3, 14)
    imageID = 13022
    GridAttr = (0,)

class QQTMapElem13024(QQTMapElem):
    offset = (2, 43)
    imageID = 13024
    GridAttr = (0,)

class QQTMapElem13034(QQTMapElem):
    offset = (0, 35)
    imageID = 13034
    GridAttr = (0,)

class QQTMapElem13035(QQTMapElem):
    offset = (0, 47)
    size = (2, 1)
    imageID = 13035
    GridAttr = (0, 0)

class QQTMapElem13036(QQTMapElem):
    offset = (0, 80)
    size = (2, 1)
    imageID = 13036
    GridAttr = (0, 0)

class QQTMapElem13037(QQTMapElem):
    offset = (0, 6)
    size = (2, 1)
    imageID = 13037
    GridAttr = (0, 0)

class QQTMapElem13038(QQTMapElem):
    offset = (0, 6)
    size = (2, 1)
    imageID = 13038
    GridAttr = (0, 0)

class QQTMapElem13039(QQTMapElem):
    offset = (-6, 44)
    size = (2, 1)
    imageID = 13039
    GridAttr = (0, 0)

class QQTMapElem13040(QQTMapElem):
    offset = (-2, 6)
    size = (2, 2)
    imageID = 13040
    GridAttr = (0, 0, 0, 0)

class QQTMapElem13042(QQTMapElem):
    offset = (0, 38)
    size = (5, 2)
    imageID = 13042
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem13043(QQTMapElem):
    offset = (-3, 62)
    size = (3, 1)
    imageID = 13043
    GridAttr = (0, 0, 0)

class QQTMapElem13044(QQTMapElem):
    offset = (-10, 58)
    size = (4, 1)
    imageID = 13044
    GridAttr = (0, 0, 0, 0)

class QQTMapElem13045(QQTMapElem):
    offset = (-1, 66)
    size = (2, 1)
    imageID = 13045
    GridAttr = (0, 0)

class QQTMapElem13046(QQTMapElem):
    offset = (-8, 69)
    size = (3, 1)
    imageID = 13046
    GridAttr = (0, 0, 0)

class QQTMapElem13050(QQTMapElem):
    imageID = 13050
    GridAttr = (3851,)

class QQTMapElem11003(QQTMapElem):
    LifeTime = 1
    offset = (4, 11)
    imageID = 11003
    GridAttr = (0,)

class QQTMapElem11004(QQTMapElem):
    offset = (1, 0)
    size = (15, 4)
    imageID = 11004
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem11005(QQTMapElem):
    size = (1, 9)
    imageID = 11005
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem13054(QQTMapElem):
    size = (15, 1)
    imageID = 13054
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem11007(QQTMapElem):
    size = (13, 1)
    imageID = 11007
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem11008(QQTMapElem):
    offset = (3, 12)
    imageID = 11008
    GridAttr = (0,)

class QQTMapElem11009(QQTMapElem):
    offset = (1, 14)
    imageID = 11009
    GridAttr = (0,)

class QQTMapElem13058(QQTMapElem):
    offset = (4, 21)
    imageID = 13058
    GridAttr = (0,)

class QQTMapElem13059(QQTMapElem):
    offset = (0, 53)
    size = (5, 1)
    imageID = 13059
    GridAttr = (0, 0, 0, 0, 0)

class QQTMapElem13060(QQTMapElem):
    offset = (-1, 35)
    size = (2, 1)
    imageID = 13060
    GridAttr = (0, 0)

class QQTMapElem13061(QQTMapElem):
    offset = (-2, 31)
    size = (2, 1)
    imageID = 13061
    GridAttr = (0, 0)

class QQTMapElem13062(QQTMapElem):
    offset = (0, 31)
    size = (2, 1)
    imageID = 13062
    GridAttr = (0, 0)

class QQTMapElem13063(QQTMapElem):
    offset = (0, 25)
    imageID = 13063
    GridAttr = (0,)

class QQTMapElem13064(QQTMapElem):
    LifeTime = 1
    offset = (2, 17)
    imageID = 13064
    GridAttr = (0,)

class QQTMapElem13065(QQTMapElem):
    LifeTime = 1
    offset = (2, 17)
    imageID = 13065
    GridAttr = (0,)

class QQTMapElem13066(QQTMapElem):
    LifeTime = 1
    offset = (1, 17)
    imageID = 13066
    GridAttr = (0,)

class QQTMapElem13067(QQTMapElem):
    LifeTime = 1
    offset = (1, 17)
    imageID = 13067
    GridAttr = (0,)

class QQTMapElem13068(QQTMapElem):
    offset = (1, 17)
    imageID = 13068
    GridAttr = (0,)

class QQTMapElem13069(QQTMapElem):
    offset = (2, 17)
    imageID = 13069
    GridAttr = (0,)

class QQTMapElem13070(QQTMapElem):
    offset = (1, 16)
    imageID = 13070
    GridAttr = (0,)

class QQTMapElem13071(QQTMapElem):
    offset = (0, 15)
    imageID = 13071
    GridAttr = (0,)

class QQTMapElem13072(QQTMapElem):
    offset = (1, 20)
    imageID = 13072
    GridAttr = (0,)

class QQTMapElem13073(QQTMapElem):
    offset = (1, 16)
    imageID = 13073
    GridAttr = (0,)

class QQTMapElem13074(QQTMapElem):
    offset = (1, 16)
    imageID = 13074
    GridAttr = (0,)

class QQTMapElem13075(QQTMapElem):
    offset = (2, 26)
    imageID = 13075
    GridAttr = (0,)

class QQTMapElem13076(QQTMapElem):
    offset = (0, 37)
    size = (2, 1)
    imageID = 13076
    GridAttr = (0, 0)

class QQTMapElem13077(QQTMapElem):
    offset = (0, 37)
    size = (2, 1)
    imageID = 13077
    GridAttr = (0, 0)

class QQTMapElem13078(QQTMapElem):
    offset = (0, -2)
    imageID = 13078
    GridAttr = (0,)

class QQTMapElem13079(QQTMapElem):
    size = (10, 1)
    imageID = 13079
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem4050(QQTMapElem):
    size = (1, 2)
    imageID = 4050
    GridAttr = (0, 0)

class QQTMapElem9003(QQTMapElem):
    offset = (2, 81)
    imageID = 9003
    GridAttr = (0,)

class QQTMapElem9004(QQTMapElem):
    offset = (1, 62)
    size = (4, 3)
    imageID = 9004
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem9005(QQTMapElem):
    offset = (3, 65)
    size = (3, 2)
    imageID = 9005
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem9006(QQTMapElem):
    offset = (2, 14)
    size = (2, 2)
    imageID = 9006
    GridAttr = (0, 0, 0, 0)

class QQTMapElem9007(QQTMapElem):
    canDoSpecial = 3
    offset = (-1, 23)
    size = (2, 1)
    imageID = 9007
    GridAttr = (0, 0)

class QQTMapElem9008(QQTMapElem):
    canMove = 2
    canDoSpecial = 3
    offset = (0, 22)
    size = (2, 1)
    imageID = 9008
    GridAttr = (0, 0)

class QQTMapElem9009(QQTMapElem):
    offset = (3, 15)
    imageID = 9009
    GridAttr = (0,)

class QQTMapElem9010(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (5, 21)
    imageID = 9010
    GridAttr = (0,)

class QQTMapElem9011(QQTMapElem):
    LifeTime = 1
    offset = (1, 11)
    imageID = 9011
    GridAttr = (0,)

class QQTMapElem9012(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (1, 11)
    imageID = 9012
    GridAttr = (0,)

class QQTMapElem9013(QQTMapElem):
    offset = (2, 41)
    imageID = 9013
    GridAttr = (5397,)
    canHide = 1

class QQTMapElem9014(QQTMapElem):
    offset = (21, 81)
    imageID = 9014
    GridAttr = (0,)

class QQTMapElem7003(QQTMapElem):
    offset = (11, 39)
    size = (6, 1)
    imageID = 7003
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem7004(QQTMapElem):
    offset = (11, 35)
    size = (6, 1)
    imageID = 7004
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem7005(QQTMapElem):
    offset = (4, 3)
    imageID = 7005
    GridAttr = (0,)

class QQTMapElem7006(QQTMapElem):
    offset = (4, 3)
    imageID = 7006
    GridAttr = (0,)

class QQTMapElem7007(QQTMapElem):
    offset = (0, 4)
    size = (1, 3)
    imageID = 7007
    GridAttr = (0, 0, 0)

class QQTMapElem7008(QQTMapElem):
    offset = (8, 3)
    size = (1, 3)
    imageID = 7008
    GridAttr = (0, 0, 0)

class QQTMapElem7010(QQTMapElem):
    offset = (-6, 16)
    imageID = 7010
    GridAttr = (0,)

class QQTMapElem7011(QQTMapElem):
    offset = (2, 30)
    size = (3, 1)
    imageID = 7011
    GridAttr = (0, 0, 0)

class QQTMapElem18241(QQTMapElem):
    imageID = 18241
    GridAttr = (3840,)

class QQTMapElem5002(QQTMapElem):
    LifeTime = 1
    canDoSpecial = 8
    offset = (5, 12)
    imageID = 5002
    GridAttr = (0,)

class QQTMapElem5003(QQTMapElem):
    LifeTime = 1
    offset = (1, 21)
    imageID = 5003
    GridAttr = (0,)

class QQTMapElem5004(QQTMapElem):
    LifeTime = 1
    offset = (2, 20)
    imageID = 5004
    GridAttr = (0,)

class QQTMapElem5005(QQTMapElem):
    offset = (1, 22)
    imageID = 5005
    GridAttr = (0,)

class QQTMapElem5006(QQTMapElem):
    offset = (-1, 12)
    imageID = 5006
    GridAttr = (0,)

class QQTMapElem5007(QQTMapElem):
    offset = (4, 12)
    imageID = 5007
    GridAttr = (0,)

class QQTMapElem5008(QQTMapElem):
    offset = (4, 12)
    imageID = 5008
    GridAttr = (0,)

class QQTMapElem5009(QQTMapElem):
    offset = (4, 14)
    size = (3, 2)
    imageID = 5009
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem5010(QQTMapElem):
    offset = (0, 18)
    imageID = 5010
    GridAttr = (5397,)
    canHide = 1

class QQTMapElem5011(QQTMapElem):
    offset = (0, 1)
    size = (4, 2)
    imageID = 5011
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem5012(QQTMapElem):
    offset = (0, 22)
    imageID = 5012
    GridAttr = (0,)

class QQTMapElem5013(QQTMapElem):
    offset = (0, 7)
    imageID = 5013
    GridAttr = (0,)

class QQTMapElem5014(QQTMapElem):
    LifeTime = 1
    offset = (0, 15)
    imageID = 5014
    GridAttr = (0,)

class QQTMapElem5015(QQTMapElem):
    offset = (4, 10)
    imageID = 5015
    GridAttr = (0,)

class QQTMapElem5016(QQTMapElem):
    offset = (5, 10)
    imageID = 5016
    GridAttr = (0,)

class QQTMapElem5017(QQTMapElem):
    LifeTime = 1
    offset = (5, 12)
    imageID = 5017
    GridAttr = (0,)

class QQTMapElem5018(QQTMapElem):
    offset = (4, 12)
    imageID = 5018
    GridAttr = (0,)

class QQTMapElem5020(QQTMapElem):
    LifeTime = 1
    canDoSpecial = 8
    offset = (0, 10)
    imageID = 5020
    GridAttr = (0,)

class QQTMapElem5021(QQTMapElem):
    offset = (1, 10)
    imageID = 5021
    GridAttr = (0,)

class QQTMapElem5023(QQTMapElem):
    imageID = 5023
    GridAttr = (0,)

class QQTMapElem5024(QQTMapElem):
    LifeTime = 1
    offset = (4, 11)
    imageID = 5024
    GridAttr = (0,)

class QQTMapElem5025(QQTMapElem):
    offset = (4, 13)
    imageID = 5025
    GridAttr = (0,)

class QQTMapElem5026(QQTMapElem):
    offset = (1, 21)
    imageID = 5026
    GridAttr = (0,)

class QQTMapElem5028(QQTMapElem):
    offset = (5, 9)
    imageID = 5028
    GridAttr = (0,)

class QQTMapElem5029(QQTMapElem):
    LifeTime = 1
    offset = (0, 9)
    imageID = 5029
    GridAttr = (0,)

class QQTMapElem5030(QQTMapElem):
    offset = (0, 11)
    imageID = 5030
    GridAttr = (0,)

class QQTMapElem5034(QQTMapElem):
    offset = (17, 49)
    size = (2, 1)
    imageID = 5034
    GridAttr = (0, 0)

class QQTMapElem5035(QQTMapElem):
    offset = (0, 74)
    size = (5, 2)
    imageID = 5035
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem5036(QQTMapElem):
    size = (15, 2)
    imageID = 5036
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem5037(QQTMapElem):
    offset = (1, 3)
    imageID = 5037
    GridAttr = (0,)

class QQTMapElem3004(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 13)
    imageID = 3004
    GridAttr = (0,)

class QQTMapElem3005(QQTMapElem):
    offset = (2, 34)
    imageID = 3005
    GridAttr = (5397,)
    canHide = 1

class QQTMapElem4057(QQTMapElem):
    offset = (-1, 44)
    imageID = 4057
    GridAttr = (0,)

class QQTMapElem3007(QQTMapElem):
    offset = (3, 17)
    imageID = 3007
    GridAttr = (0,)

class QQTMapElem3008(QQTMapElem):
    offset = (3, 17)
    imageID = 3008
    GridAttr = (0,)

class QQTMapElem3009(QQTMapElem):
    offset = (3, 18)
    imageID = 3009
    GridAttr = (0,)

class QQTMapElem3010(QQTMapElem):
    offset = (2, 13)
    imageID = 3010
    GridAttr = (0,)

class QQTMapElem3011(QQTMapElem):
    imageID = 3011
    GridAttr = (0,)

class QQTMapElem3012(QQTMapElem):
    imageID = 3012
    GridAttr = (0,)

class QQTMapElem3013(QQTMapElem):
    imageID = 3013
    GridAttr = (0,)

class QQTMapElem3014(QQTMapElem):
    LifeTime = 1
    offset = (3, 10)
    imageID = 3014
    GridAttr = (0,)

class QQTMapElem3015(QQTMapElem):
    LifeTime = 1
    offset = (2, 10)
    imageID = 3015
    GridAttr = (0,)

class QQTMapElem3017(QQTMapElem):
    LifeTime = 1
    offset = (2, 10)
    imageID = 3017
    GridAttr = (0,)

class QQTMapElem3018(QQTMapElem):
    LifeTime = 1
    offset = (2, 10)
    imageID = 3018
    GridAttr = (0,)

class QQTMapElem3019(QQTMapElem):
    offset = (0, 30)
    size = (4, 2)
    imageID = 3019
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem3020(QQTMapElem):
    offset = (0, 14)
    imageID = 3020
    GridAttr = (0,)

class QQTMapElem3022(QQTMapElem):
    imageID = 3022
    GridAttr = (0,)

class QQTMapElem3023(QQTMapElem):
    imageID = 3023
    GridAttr = (0,)

class QQTMapElem3024(QQTMapElem):
    imageID = 3024
    GridAttr = (0,)

class QQTMapElem3025(QQTMapElem):
    imageID = 3025
    GridAttr = (0,)

class QQTMapElem3026(QQTMapElem):
    imageID = 3026
    GridAttr = (0,)

class QQTMapElem3050(QQTMapElem):
    offset = (1, 60)
    imageID = 3050
    GridAttr = (0,)

class QQTMapElem1003(QQTMapElem):
    LifeTime = 1
    offset = (3, 11)
    imageID = 1003
    GridAttr = (0,)

class QQTMapElem1004(QQTMapElem):
    offset = (3, 10)
    imageID = 1004
    GridAttr = (0,)

class QQTMapElem1005(QQTMapElem):
    offset = (2, 20)
    imageID = 1005
    GridAttr = (0,)

class QQTMapElem1006(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (4, 23)
    imageID = 1006
    GridAttr = (0,)

class QQTMapElem1007(QQTMapElem):
    offset = (4, 29)
    size = (4, 3)
    imageID = 1007
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem1008(QQTMapElem):
    offset = (4, 24)
    imageID = 1008
    GridAttr = (5397,)
    canHide = 1

class QQTMapElem1009(QQTMapElem):
    offset = (2, 20)
    imageID = 1009
    GridAttr = (0,)

class QQTMapElem3058(QQTMapElem):
    offset = (0, 22)
    size = (15, 3)
    imageID = 3058
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem1011(QQTMapElem):
    offset = (2, 31)
    imageID = 1011
    GridAttr = (0,)

class QQTMapElem3060(QQTMapElem):
    offset = (21, 51)
    imageID = 3060
    GridAttr = (0,)

class QQTMapElem3061(QQTMapElem):
    offset = (2, 51)
    imageID = 3061
    GridAttr = (0,)

class QQTMapElem18242(QQTMapElem):
    imageID = 18242
    GridAttr = (0,)

class QQTMapElem4059(QQTMapElem):
    size = (1, 2)
    imageID = 4059
    GridAttr = (0, 0)

class QQTMapElem3120(QQTMapElem):
    size = (1, 2)
    imageID = 3120
    GridAttr = (0, 0)

class QQTMapElem3121(QQTMapElem):
    size = (1, 2)
    imageID = 3121
    GridAttr = (0, 0)

class QQTMapElem3122(QQTMapElem):
    size = (1, 2)
    imageID = 3122
    GridAttr = (5, 5)

class QQTMapElem4060(QQTMapElem):
    size = (1, 2)
    imageID = 4060
    GridAttr = (0, 0)

class QQTMapElem14110(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (1, 15)
    imageID = 14110
    GridAttr = (0,)

class QQTMapElem1113(QQTMapElem):
    imageID = 1113
    GridAttr = (0,)

class QQTMapElem1114(QQTMapElem):
    size = (8, 2)
    imageID = 1114
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem1115(QQTMapElem):
    size = (1, 4)
    imageID = 1115
    GridAttr = (0, 0, 0, 0)

class QQTMapElem1116(QQTMapElem):
    imageID = 1116
    GridAttr = (0,)

class QQTMapElem1117(QQTMapElem):
    size = (2, 1)
    imageID = 1117
    GridAttr = (0, 0)

class QQTMapElem1118(QQTMapElem):
    size = (2, 1)
    imageID = 1118
    GridAttr = (0, 0)

class QQTMapElem1119(QQTMapElem):
    size = (2, 4)
    imageID = 1119
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem1120(QQTMapElem):
    size = (11, 2)
    imageID = 1120
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem1121(QQTMapElem):
    size = (6, 2)
    imageID = 1121
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem1122(QQTMapElem):
    size = (2, 3)
    imageID = 1122
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem1123(QQTMapElem):
    size = (7, 2)
    imageID = 1123
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem1124(QQTMapElem):
    size = (1, 3)
    imageID = 1124
    GridAttr = (0, 0, 0)

class QQTMapElem1125(QQTMapElem):
    size = (1, 3)
    imageID = 1125
    GridAttr = (0, 0, 0)

class QQTMapElem1126(QQTMapElem):
    size = (14, 2)
    imageID = 1126
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem1127(QQTMapElem):
    size = (1, 6)
    imageID = 1127
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem1128(QQTMapElem):
    size = (6, 2)
    imageID = 1128
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem1129(QQTMapElem):
    size = (1, 2)
    imageID = 1129
    GridAttr = (0, 0)

class QQTMapElem1130(QQTMapElem):
    size = (2, 4)
    imageID = 1130
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem1131(QQTMapElem):
    size = (2, 2)
    imageID = 1131
    GridAttr = (0, 0, 0, 0)

class QQTMapElem1132(QQTMapElem):
    offset = (0, -1)
    size = (1, 6)
    imageID = 1132
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem1133(QQTMapElem):
    size = (2, 2)
    imageID = 1133
    GridAttr = (0, 0, 0, 0)

class QQTMapElem1134(QQTMapElem):
    size = (8, 2)
    imageID = 1134
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem1135(QQTMapElem):
    size = (11, 2)
    imageID = 1135
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem1136(QQTMapElem):
    size = (11, 2)
    imageID = 1136
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem1137(QQTMapElem):
    size = (7, 2)
    imageID = 1137
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem1138(QQTMapElem):
    imageID = 1138
    GridAttr = (0,)

class QQTMapElem1139(QQTMapElem):
    size = (1, 3)
    imageID = 1139
    GridAttr = (0, 0, 0)

class QQTMapElem1140(QQTMapElem):
    size = (1, 2)
    imageID = 1140
    GridAttr = (0, 0)

class QQTMapElem1141(QQTMapElem):
    size = (11, 2)
    imageID = 1141
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem6013(QQTMapElem):
    offset = (4, 25)
    imageID = 6013
    GridAttr = (0,)

class QQTMapElem4007(QQTMapElem):
    offset = (0, 26)
    imageID = 4007
    GridAttr = (0,)

class QQTMapElem2015(QQTMapElem):
    LifeTime = 1
    offset = (2, 11)
    imageID = 2015
    GridAttr = (0,)

class QQTMapElem4013(QQTMapElem):
    imageID = 4013
    GridAttr = (3840,)

class QQTMapElem10009(QQTMapElem):
    offset = (1, 2)
    size = (3, 3)
    imageID = 10009
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem4021(QQTMapElem):
    imageID = 4021
    GridAttr = (3840,)

class QQTMapElem18002(QQTMapElem):
    size = (1, 4)
    imageID = 18002
    GridAttr = (0, 0, 0, 0)

class QQTMapElem18003(QQTMapElem):
    imageID = 18003
    GridAttr = (13,)

class QQTMapElem18004(QQTMapElem):
    size = (2, 1)
    imageID = 18004
    GridAttr = (0, 0)

class QQTMapElem18005(QQTMapElem):
    size = (2, 1)
    imageID = 18005
    GridAttr = (0, 0)

class QQTMapElem18006(QQTMapElem):
    offset = (0, 1)
    size = (2, 4)
    imageID = 18006
    GridAttr = (0, 0, 0, 0, 0, 2, 0, 0)

class QQTMapElem18007(QQTMapElem):
    size = (11, 2)
    imageID = 18007
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem18008(QQTMapElem):
    size = (6, 2)
    imageID = 18008
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem18009(QQTMapElem):
    size = (2, 3)
    imageID = 18009
    GridAttr = (4096, 0, 0, 3, 0, 0)

class QQTMapElem18020(QQTMapElem):
    size = (2, 2)
    imageID = 18020
    GridAttr = (0, 0, 0, 0)

class QQTMapElem18021(QQTMapElem):
    size = (8, 2)
    imageID = 18021
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem18022(QQTMapElem):
    size = (11, 2)
    imageID = 18022
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem18023(QQTMapElem):
    size = (11, 2)
    imageID = 18023
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem18024(QQTMapElem):
    size = (7, 2)
    imageID = 18024
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem18025(QQTMapElem):
    imageID = 18025
    GridAttr = (0,)

class QQTMapElem18026(QQTMapElem):
    size = (1, 3)
    imageID = 18026
    GridAttr = (0, 0, 0)

class QQTMapElem18027(QQTMapElem):
    size = (1, 2)
    imageID = 18027
    GridAttr = (0, 0)

class QQTMapElem18028(QQTMapElem):
    size = (11, 2)
    imageID = 18028
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem16001(QQTMapElem):
    offset = (2, 2)
    size = (2, 2)
    imageID = 16001
    GridAttr = (3840, 3840, 3840, 3840)

class QQTMapElem16002(QQTMapElem):
    offset = (3, 3)
    imageID = 16002
    GridAttr = (3840,)

class QQTMapElem16003(QQTMapElem):
    offset = (2, 3)
    size = (3, 1)
    imageID = 16003
    GridAttr = (3840, 3840, 3840)

class QQTMapElem16004(QQTMapElem):
    offset = (2, 2)
    size = (1, 3)
    imageID = 16004
    GridAttr = (3840, 3840, 3840)

class QQTMapElem16005(QQTMapElem):
    LifeTime = 1
    offset = (1, 0)
    imageID = 16005
    GridAttr = (0,)

class QQTMapElem16006(QQTMapElem):
    offset = (-7, 9)
    size = (8, 1)
    imageID = 16006
    GridAttr = (3840, 3840, 3840, 3840, 3840, 3840, 3840, 3840)

class QQTMapElem16007(QQTMapElem):
    offset = (5, -3)
    size = (4, 1)
    imageID = 16007
    GridAttr = (3840, 3840, 3840, 3840)

class QQTMapElem16008(QQTMapElem):
    offset = (15, -11)
    size = (1, 8)
    imageID = 16008
    GridAttr = (3840, 3840, 3840, 3840, 3840, 3840, 3840, 3840)

class QQTMapElem16009(QQTMapElem):
    offset = (0, 2)
    size = (1, 4)
    imageID = 16009
    GridAttr = (3840, 3840, 3840, 3840)

class QQTMapElem16011(QQTMapElem):
    offset = (7, 10)
    imageID = 16011
    GridAttr = (0,)

class QQTMapElem16012(QQTMapElem):
    offset = (4, 11)
    size = (2, 2)
    imageID = 16012
    GridAttr = (0, 0, 0, 0)

class QQTMapElem16013(QQTMapElem):
    offset = (9, 12)
    size = (4, 1)
    imageID = 16013
    GridAttr = (0, 0, 0, 0)

class QQTMapElem16014(QQTMapElem):
    offset = (7, 10)
    size = (1, 4)
    imageID = 16014
    GridAttr = (0, 0, 0, 0)

class QQTMapElem16015(QQTMapElem):
    offset = (6, 6)
    size = (3, 3)
    imageID = 16015
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem16016(QQTMapElem):
    offset = (2, 2)
    imageID = 16016
    GridAttr = (3840,)

class QQTMapElem16017(QQTMapElem):
    offset = (1, 2)
    size = (3, 1)
    imageID = 16017
    GridAttr = (3840, 3840, 3840)

class QQTMapElem16018(QQTMapElem):
    offset = (2, 2)
    size = (1, 3)
    imageID = 16018
    GridAttr = (3840, 3840, 3840)

class QQTMapElem16019(QQTMapElem):
    offset = (1, 1)
    size = (2, 2)
    imageID = 16019
    GridAttr = (3840, 3840, 3840, 3840)

class QQTMapElem16020(QQTMapElem):
    LifeTime = 2
    offset = (1, 0)
    imageID = 16020
    GridAttr = (0,)

class QQTMapElem16021(QQTMapElem):
    offset = (1, 0)
    size = (1, 4)
    imageID = 16021
    GridAttr = (0, 0, 0, 0)

class QQTMapElem16022(QQTMapElem):
    offset = (1, 10)
    size = (4, 1)
    imageID = 16022
    GridAttr = (0, 0, 0, 0)

class QQTMapElem16023(QQTMapElem):
    offset = (1, 0)
    size = (4, 1)
    imageID = 16023
    GridAttr = (0, 0, 0, 0)

class QQTMapElem16024(QQTMapElem):
    offset = (11, 0)
    size = (1, 4)
    imageID = 16024
    GridAttr = (0, 0, 0, 0)

class QQTMapElem16025(QQTMapElem):
    LifeTime = 1
    offset = (4, 11)
    imageID = 16025
    GridAttr = (0,)

class QQTMapElem16026(QQTMapElem):
    imageID = 16026
    GridAttr = (0,)

class QQTMapElem16027(QQTMapElem):
    imageID = 16027
    GridAttr = (0,)

class QQTMapElem16028(QQTMapElem):
    imageID = 16028
    GridAttr = (0,)

class QQTMapElem16029(QQTMapElem):
    imageID = 16029
    GridAttr = (0,)

class QQTMapElem16030(QQTMapElem):
    imageID = 16030
    GridAttr = (0,)

class QQTMapElem16031(QQTMapElem):
    imageID = 16031
    GridAttr = (0,)

class QQTMapElem16032(QQTMapElem):
    imageID = 16032
    GridAttr = (0,)

class QQTMapElem16033(QQTMapElem):
    imageID = 16033
    GridAttr = (0,)

class QQTMapElem16034(QQTMapElem):
    imageID = 16034
    GridAttr = (0,)

class QQTMapElem16035(QQTMapElem):
    imageID = 16035
    GridAttr = (0,)

class QQTMapElem16036(QQTMapElem):
    imageID = 16036
    GridAttr = (0,)

class QQTMapElem16037(QQTMapElem):
    imageID = 16037
    GridAttr = (0,)

class QQTMapElem16038(QQTMapElem):
    imageID = 16038
    GridAttr = (0,)

class QQTMapElem18101(QQTMapElem):
    size = (7, 2)
    imageID = 18101
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem18102(QQTMapElem):
    size = (1, 3)
    imageID = 18102
    GridAttr = (0, 0, 0)

class QQTMapElem18103(QQTMapElem):
    size = (14, 2)
    imageID = 18103
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem18104(QQTMapElem):
    size = (1, 6)
    imageID = 18104
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem18105(QQTMapElem):
    size = (6, 2)
    imageID = 18105
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem18106(QQTMapElem):
    size = (1, 2)
    imageID = 18106
    GridAttr = (0, 0)

class QQTMapElem18107(QQTMapElem):
    size = (2, 4)
    imageID = 18107
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem18108(QQTMapElem):
    size = (2, 2)
    imageID = 18108
    GridAttr = (0, 0, 0, 0)

class QQTMapElem18109(QQTMapElem):
    size = (1, 6)
    imageID = 18109
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem18111(QQTMapElem):
    size = (8, 2)
    imageID = 18111
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem18112(QQTMapElem):
    size = (1, 3)
    imageID = 18112
    GridAttr = (0, 0, 0)

class QQTMapElem14022(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 12)
    imageID = 14022
    GridAttr = (0,)

class QQTMapElem14023(QQTMapElem):
    LifeTime = 1
    canMove = 2
    canDoSpecial = 11
    offset = (2, 5)
    imageID = 14023
    GridAttr = (0,)

class QQTMapElem14024(QQTMapElem):
    offset = (2, 42)
    imageID = 14024
    GridAttr = (0,)

class QQTMapElem14025(QQTMapElem):
    offset = (3, 27)
    imageID = 14025
    GridAttr = (0,)

class QQTMapElem14026(QQTMapElem):
    offset = (3, 26)
    imageID = 14026
    GridAttr = (0,)

class QQTMapElem14027(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (3, 12)
    imageID = 14027
    GridAttr = (0,)

class QQTMapElem14028(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (0, 10)
    imageID = 14028
    GridAttr = (0,)

class QQTMapElem14029(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 12)
    imageID = 14029
    GridAttr = (0,)

class QQTMapElem14030(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 16)
    imageID = 14030
    GridAttr = (0,)

class QQTMapElem14031(QQTMapElem):
    LifeTime = 1
    canMove = 6
    canDoSpecial = 4
    offset = (0, 20)
    imageID = 14031
    GridAttr = (0,)

class QQTMapElem14032(QQTMapElem):
    offset = (3, 26)
    imageID = 14032
    GridAttr = (0,)

class QQTMapElem14033(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 16)
    imageID = 14033
    GridAttr = (0,)

class QQTMapElem14036(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 12)
    imageID = 14036
    GridAttr = (0,)

class QQTMapElem14038(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (3, 12)
    imageID = 14038
    GridAttr = (0,)

class QQTMapElem14039(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (1, 13)
    imageID = 14039
    GridAttr = (0,)

class QQTMapElem14040(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 12)
    imageID = 14040
    GridAttr = (0,)

class QQTMapElem14041(QQTMapElem):
    LifeTime = 1
    canMove = 10
    canDoSpecial = 5
    offset = (2, 18)
    imageID = 14041
    GridAttr = (0,)

class QQTMapElem14042(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (1, 11)
    imageID = 14042
    GridAttr = (0,)

class QQTMapElem14043(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 13)
    imageID = 14043
    GridAttr = (0,)

class QQTMapElem14044(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 13)
    imageID = 14044
    GridAttr = (0,)

class QQTMapElem14045(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 13)
    imageID = 14045
    GridAttr = (0,)

class QQTMapElem14046(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 13)
    imageID = 14046
    GridAttr = (0,)

class QQTMapElem14047(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 13)
    imageID = 14047
    GridAttr = (0,)

class QQTMapElem14048(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 12)
    imageID = 14048
    GridAttr = (0,)

class QQTMapElem14049(QQTMapElem):
    LifeTime = 1
    offset = (2, 13)
    imageID = 14049
    GridAttr = (0,)

class QQTMapElem12002(QQTMapElem):
    LifeTime = 1
    offset = (0, 14)
    imageID = 12002
    GridAttr = (0,)

class QQTMapElem12003(QQTMapElem):
    LifeTime = 1
    offset = (2, 13)
    imageID = 12003
    GridAttr = (0,)

class QQTMapElem12004(QQTMapElem):
    LifeTime = 1
    offset = (2, 14)
    imageID = 12004
    GridAttr = (0,)

class QQTMapElem16102(QQTMapElem):
    LifeTime = 1
    offset = (3, 14)
    imageID = 16102
    GridAttr = (0,)

class QQTMapElem16103(QQTMapElem):
    LifeTime = 1
    offset = (0, 8)
    imageID = 16103
    GridAttr = (0,)

class QQTMapElem16104(QQTMapElem):
    LifeTime = 1
    offset = (3, 9)
    imageID = 16104
    GridAttr = (7967,)
    canHide = 1

class QQTMapElem12009(QQTMapElem):
    canDoSpecial = 2
    offset = (6, 41)
    imageID = 12009
    GridAttr = (7967,)
    canHide = 1

class QQTMapElem16106(QQTMapElem):
    LifeTime = 1
    offset = (2, 10)
    imageID = 16106
    GridAttr = (0,)

class QQTMapElem12011(QQTMapElem):
    offset = (2, 29)
    imageID = 12011
    GridAttr = (5397,)
    canHide = 1

class QQTMapElem16108(QQTMapElem):
    LifeTime = 1
    offset = (4, 14)
    imageID = 16108
    GridAttr = (0,)

class QQTMapElem16109(QQTMapElem):
    LifeTime = 1
    offset = (4, 11)
    imageID = 16109
    GridAttr = (0,)

class QQTMapElem16110(QQTMapElem):
    offset = (5, 22)
    imageID = 16110
    GridAttr = (0,)

class QQTMapElem16111(QQTMapElem):
    offset = (0, 53)
    size = (3, 1)
    imageID = 16111
    GridAttr = (0, 1285, 0)

class QQTMapElem16112(QQTMapElem):
    LifeTime = 1
    offset = (3, 9)
    imageID = 16112
    GridAttr = (7967,)
    canHide = 1

class QQTMapElem16113(QQTMapElem):
    offset = (1, 5)
    imageID = 16113
    GridAttr = (0,)

class QQTMapElem16114(QQTMapElem):
    offset = (4, 26)
    imageID = 16114
    GridAttr = (5397,)
    canHide = 1

class QQTMapElem2003(QQTMapElem):
    LifeTime = 1
    canMove = 2
    canDoSpecial = 10
    offset = (2, 5)
    imageID = 2003
    GridAttr = (0,)

class QQTMapElem12020(QQTMapElem):
    LifeTime = 1
    offset = (2, 13)
    imageID = 12020
    GridAttr = (0,)

class QQTMapElem12021(QQTMapElem):
    LifeTime = 1
    offset = (2, 13)
    imageID = 12021
    GridAttr = (0,)

class QQTMapElem4052(QQTMapElem):
    offset = (1, 37)
    imageID = 4052
    GridAttr = (0,)

class QQTMapElem4053(QQTMapElem):
    offset = (1, 43)
    imageID = 4053
    GridAttr = (0,)

class QQTMapElem4054(QQTMapElem):
    offset = (1, 43)
    imageID = 4054
    GridAttr = (0,)

class QQTMapElem14108(QQTMapElem):
    offset = (5, 15)
    imageID = 14108
    GridAttr = (0,)

class QQTMapElem4055(QQTMapElem):
    imageID = 4055
    GridAttr = (0,)

class QQTMapElem10002(QQTMapElem):
    imageID = 10002
    GridAttr = (0,)

class QQTMapElem10003(QQTMapElem):
    imageID = 10003
    GridAttr = (0,)

class QQTMapElem14100(QQTMapElem):
    LifeTime = 1
    canMove = 10
    canDoSpecial = 5
    offset = (2, 12)
    imageID = 14100
    GridAttr = (0,)

class QQTMapElem10005(QQTMapElem):
    LifeTime = 1
    offset = (2, 12)
    imageID = 10005
    GridAttr = (0,)

class QQTMapElem10006(QQTMapElem):
    offset = (0, 19)
    imageID = 10006
    GridAttr = (0,)

class QQTMapElem10007(QQTMapElem):
    LifeTime = 1
    canMove = 2
    canDoSpecial = 7
    offset = (2, 13)
    imageID = 10007
    GridAttr = (0,)

class QQTMapElem14104(QQTMapElem):
    offset = (1, 13)
    imageID = 14104
    GridAttr = (0,)

class QQTMapElem14105(QQTMapElem):
    LifeTime = 1
    canMove = 6
    canDoSpecial = 4
    offset = (2, 5)
    imageID = 14105
    GridAttr = (0,)

class QQTMapElem14106(QQTMapElem):
    offset = (3, 22)
    imageID = 14106
    GridAttr = (6682,)
    canHide = 1

class QQTMapElem14107(QQTMapElem):
    offset = (4, 38)
    size = (3, 3)
    imageID = 14107
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem10012(QQTMapElem):
    offset = (-1, 45)
    imageID = 10012
    GridAttr = (0,)

class QQTMapElem14109(QQTMapElem):
    offset = (5, 15)
    imageID = 14109
    GridAttr = (0,)

class QQTMapElem10014(QQTMapElem):
    offset = (0, 41)
    imageID = 10014
    GridAttr = (6682,)
    canHide = 1

class QQTMapElem10015(QQTMapElem):
    imageID = 10015
    GridAttr = (0,)

class QQTMapElem14112(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (3, 15)
    imageID = 14112
    GridAttr = (0,)

class QQTMapElem10017(QQTMapElem):
    imageID = 10017
    GridAttr = (0,)

class QQTMapElem14114(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 15)
    imageID = 14114
    GridAttr = (0,)

class QQTMapElem14115(QQTMapElem):
    LifeTime = 1
    canMove = 18
    canDoSpecial = 6
    offset = (2, 13)
    imageID = 14115
    GridAttr = (0,)

class QQTMapElem14116(QQTMapElem):
    imageID = 14116
    GridAttr = (3840,)

class QQTMapElem14117(QQTMapElem):
    offset = (16, 13)
    imageID = 14117
    GridAttr = (3840,)

class QQTMapElem14118(QQTMapElem):
    offset = (10, 0)
    imageID = 14118
    GridAttr = (3840,)

class QQTMapElem14119(QQTMapElem):
    offset = (0, 19)
    imageID = 14119
    GridAttr = (3840,)

class QQTMapElem14120(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 12)
    imageID = 14120
    GridAttr = (0,)

class QQTMapElem14121(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (3, 13)
    imageID = 14121
    GridAttr = (0,)

class QQTMapElem14122(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 10)
    imageID = 14122
    GridAttr = (0,)

class QQTMapElem14123(QQTMapElem):
    offset = (1, 16)
    imageID = 14123
    GridAttr = (0,)

class QQTMapElem14124(QQTMapElem):
    offset = (1, 26)
    imageID = 14124
    GridAttr = (0,)

class QQTMapElem14125(QQTMapElem):
    offset = (2, 25)
    imageID = 14125
    GridAttr = (0,)

class QQTMapElem14126(QQTMapElem):
    LifeTime = 1
    offset = (3, 13)
    imageID = 14126
    GridAttr = (0,)

class QQTMapElem14127(QQTMapElem):
    LifeTime = 1
    imageID = 14127
    GridAttr = (0,)

class QQTMapElem18229(QQTMapElem):
    offset = (10, 8)
    imageID = 18229
    GridAttr = (3840,)

class QQTMapElem18230(QQTMapElem):
    imageID = 18230
    GridAttr = (3840,)

class QQTMapElem18231(QQTMapElem):
    imageID = 18231
    GridAttr = (3840,)

class QQTMapElem18232(QQTMapElem):
    imageID = 18232
    GridAttr = (3840,)

class QQTMapElem18233(QQTMapElem):
    imageID = 18233
    GridAttr = (3840,)

class QQTMapElem18234(QQTMapElem):
    offset = (0, 7)
    imageID = 18234
    GridAttr = (3840,)

class QQTMapElem18235(QQTMapElem):
    offset = (0, 9)
    imageID = 18235
    GridAttr = (3840,)

class QQTMapElem18236(QQTMapElem):
    offset = (7, 0)
    imageID = 18236
    GridAttr = (3840,)

class QQTMapElem18237(QQTMapElem):
    imageID = 18237
    GridAttr = (3840,)

class QQTMapElem18238(QQTMapElem):
    imageID = 18238
    GridAttr = (3840,)

class QQTMapElem18239(QQTMapElem):
    offset = (10, 0)
    imageID = 18239
    GridAttr = (3840,)

class QQTMapElem18240(QQTMapElem):
    imageID = 18240
    GridAttr = (3840,)

class QQTMapElem8001(QQTMapElem):
    LifeTime = 1
    canDoSpecial = 7
    offset = (2, 10)
    imageID = 8001
    GridAttr = (0,)

class QQTMapElem8002(QQTMapElem):
    LifeTime = 1
    offset = (2, 10)
    imageID = 8002
    GridAttr = (0,)

class QQTMapElem8003(QQTMapElem):
    LifeTime = 1
    canDoSpecial = 7
    offset = (2, 10)
    imageID = 8003
    GridAttr = (0,)

class QQTMapElem8004(QQTMapElem):
    LifeTime = 1
    offset = (2, 10)
    imageID = 8004
    GridAttr = (0,)

class QQTMapElem8005(QQTMapElem):
    offset = (2, 21)
    imageID = 8005
    GridAttr = (0,)

class QQTMapElem8006(QQTMapElem):
    offset = (2, 21)
    imageID = 8006
    GridAttr = (0,)

class QQTMapElem8007(QQTMapElem):
    LifeTime = 1
    offset = (2, 17)
    imageID = 8007
    GridAttr = (0,)

class QQTMapElem8008(QQTMapElem):
    offset = (0, 45)
    size = (4, 2)
    imageID = 8008
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem8009(QQTMapElem):
    canDoSpecial = 1
    offset = (1, 20)
    size = (3, 3)
    imageID = 8009
    GridAttr = (0, 7967, 0, 7967, 7967, 7967, 0, 7967, 0)
    canHide = 1

class QQTMapElem8010(QQTMapElem):
    canDoSpecial = 2
    offset = (1, 20)
    size = (3, 3)
    imageID = 8010
    GridAttr = (0, 7967, 0, 7967, 7967, 7967, 0, 7967, 0)
    canHide = 1

class QQTMapElem8012(QQTMapElem):
    offset = (1, 21)
    imageID = 8012
    GridAttr = (0,)

class QQTMapElem8014(QQTMapElem):
    offset = (2, 19)
    size = (3, 3)
    imageID = 8014
    GridAttr = (0, 7967, 0, 7967, 7967, 7967, 0, 7967, 0)
    canHide = 1

class QQTMapElem8018(QQTMapElem):
    offset = (0, 16)
    imageID = 8018
    GridAttr = (0,)

class QQTMapElem8019(QQTMapElem):
    LifeTime = 1
    offset = (0, 19)
    imageID = 8019
    GridAttr = (0,)

class QQTMapElem8021(QQTMapElem):
    LifeTime = 3
    offset = (4, 33)
    imageID = 8021
    GridAttr = (0,)

class QQTMapElem8022(QQTMapElem):
    LifeTime = 2
    offset = (4, 16)
    imageID = 8022
    GridAttr = (0,)

class QQTMapElem8023(QQTMapElem):
    LifeTime = 1
    offset = (3, -1)
    imageID = 8023
    GridAttr = (0,)

class QQTMapElem14111(QQTMapElem):
    LifeTime = 1
    canMove = 2
    offset = (2, 16)
    imageID = 14111
    GridAttr = (0,)

class QQTMapElem6002(QQTMapElem):
    LifeTime = 1
    offset = (4, 14)
    imageID = 6002
    GridAttr = (0,)

class QQTMapElem6003(QQTMapElem):
    LifeTime = 1
    offset = (4, 12)
    imageID = 6003
    GridAttr = (7967,)
    canHide = 1

class QQTMapElem6004(QQTMapElem):
    LifeTime = 1
    offset = (4, 13)
    imageID = 6004
    GridAttr = (0,)

class QQTMapElem6005(QQTMapElem):
    LifeTime = 1
    offset = (3, 12)
    imageID = 6005
    GridAttr = (0,)

class QQTMapElem6006(QQTMapElem):
    LifeTime = 1
    offset = (-1, 11)
    imageID = 6006
    GridAttr = (0,)

class QQTMapElem6007(QQTMapElem):
    offset = (3, 14)
    imageID = 6007
    GridAttr = (0,)

class QQTMapElem6008(QQTMapElem):
    offset = (6, 22)
    imageID = 6008
    GridAttr = (0,)

class QQTMapElem6009(QQTMapElem):
    offset = (3, 16)
    imageID = 6009
    GridAttr = (0,)

class QQTMapElem6010(QQTMapElem):
    offset = (5, 23)
    imageID = 6010
    GridAttr = (0,)

class QQTMapElem6011(QQTMapElem):
    offset = (5, 33)
    size = (3, 2)
    imageID = 6011
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem6012(QQTMapElem):
    LifeTime = 1
    offset = (2, 14)
    imageID = 6012
    GridAttr = (0,)

class QQTMapElem1002(QQTMapElem):
    LifeTime = 1
    canDoSpecial = 7
    offset = (3, 11)
    imageID = 1002
    GridAttr = (0,)

class QQTMapElem6014(QQTMapElem):
    offset = (4, 26)
    imageID = 6014
    GridAttr = (0,)

class QQTMapElem6015(QQTMapElem):
    offset = (4, 26)
    imageID = 6015
    GridAttr = (0,)

class QQTMapElem6016(QQTMapElem):
    offset = (-1, 12)
    imageID = 6016
    GridAttr = (0,)

class QQTMapElem3051(QQTMapElem):
    offset = (-1, 30)
    imageID = 3051
    GridAttr = (0,)

class QQTMapElem3054(QQTMapElem):
    LifeTime = 1
    offset = (2, 12)
    imageID = 3054
    GridAttr = (0,)

class QQTMapElem3055(QQTMapElem):
    LifeTime = 1
    offset = (3, 12)
    imageID = 3055
    GridAttr = (0,)

class QQTMapElem15002(QQTMapElem):
    LifeTime = 1
    offset = (5, 12)
    imageID = 15002
    GridAttr = (0,)

class QQTMapElem3056(QQTMapElem):
    LifeTime = 1
    offset = (3, 21)
    imageID = 3056
    GridAttr = (0,)

class QQTMapElem17051(QQTMapElem):
    offset = (2, 5)
    imageID = 17051
    GridAttr = (0,)

class QQTMapElem4004(QQTMapElem):
    LifeTime = 1
    offset = (4, 11)
    imageID = 4004
    GridAttr = (0,)

class QQTMapElem4005(QQTMapElem):
    offset = (4, 22)
    imageID = 4005
    GridAttr = (0,)

class QQTMapElem4006(QQTMapElem):
    LifeTime = 1
    canMove = 2
    canDoSpecial = 9
    offset = (3, 10)
    imageID = 4006
    GridAttr = (0,)

class QQTMapElem3057(QQTMapElem):
    offset = (-2, 29)
    imageID = 3057
    GridAttr = (0,)

class QQTMapElem4008(QQTMapElem):
    LifeTime = 1
    offset = (4, 20)
    imageID = 4008
    GridAttr = (0,)

class QQTMapElem17052(QQTMapElem):
    offset = (2, 28)
    imageID = 17052
    GridAttr = (0,)

class QQTMapElem4012(QQTMapElem):
    LifeTime = 1
    offset = (4, 10)
    imageID = 4012
    GridAttr = (0,)

class QQTMapElem1010(QQTMapElem):
    offset = (4, 24)
    imageID = 1010
    GridAttr = (5397,)
    canHide = 1

class QQTMapElem4014(QQTMapElem):
    imageID = 4014
    GridAttr = (3840,)

class QQTMapElem4015(QQTMapElem):
    imageID = 4015
    GridAttr = (3840,)

class QQTMapElem4016(QQTMapElem):
    imageID = 4016
    GridAttr = (3840,)

class QQTMapElem4017(QQTMapElem):
    imageID = 4017
    GridAttr = (3840,)

class QQTMapElem4018(QQTMapElem):
    imageID = 4018
    GridAttr = (3840,)

class QQTMapElem4019(QQTMapElem):
    imageID = 4019
    GridAttr = (3840,)

class QQTMapElem4020(QQTMapElem):
    imageID = 4020
    GridAttr = (3840,)

class QQTMapElem15006(QQTMapElem):
    offset = (-1, 12)
    imageID = 15006
    GridAttr = (0,)

class QQTMapElem4022(QQTMapElem):
    imageID = 4022
    GridAttr = (3840,)

class QQTMapElem4023(QQTMapElem):
    imageID = 4023
    GridAttr = (3840,)

class QQTMapElem4024(QQTMapElem):
    imageID = 4024
    GridAttr = (3840,)

class QQTMapElem4025(QQTMapElem):
    imageID = 4025
    GridAttr = (3840,)

class QQTMapElem4026(QQTMapElem):
    imageID = 4026
    GridAttr = (3840,)

class QQTMapElem4027(QQTMapElem):
    LifeTime = 1
    offset = (4, 21)
    imageID = 4027
    GridAttr = (0,)

class QQTMapElem4028(QQTMapElem):
    offset = (1, 31)
    imageID = 4028
    GridAttr = (0,)

class QQTMapElem4029(QQTMapElem):
    offset = (1, 21)
    imageID = 4029
    GridAttr = (0,)

class QQTMapElem15008(QQTMapElem):
    offset = (4, 12)
    imageID = 15008
    GridAttr = (0,)

class QQTMapElem17057(QQTMapElem):
    offset = (0, 15)
    imageID = 17057
    GridAttr = (0,)

class QQTMapElem4040(QQTMapElem):
    size = (1, 2)
    imageID = 4040
    GridAttr = (0, 0)

class QQTMapElem4041(QQTMapElem):
    imageID = 4041
    GridAttr = (0,)

class QQTMapElem4042(QQTMapElem):
    imageID = 4042
    GridAttr = (0,)

class QQTMapElem4043(QQTMapElem):
    imageID = 4043
    GridAttr = (0,)

class QQTMapElem4044(QQTMapElem):
    imageID = 4044
    GridAttr = (0,)

class QQTMapElem17058(QQTMapElem):
    offset = (0, 25)
    size = (3, 2)
    imageID = 17058
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem4046(QQTMapElem):
    imageID = 4046
    GridAttr = (0,)

class QQTMapElem4047(QQTMapElem):
    size = (1, 2)
    imageID = 4047
    GridAttr = (0, 0)

class QQTMapElem4048(QQTMapElem):
    size = (1, 2)
    imageID = 4048
    GridAttr = (0, 0)

class QQTMapElem4049(QQTMapElem):
    size = (1, 2)
    imageID = 4049
    GridAttr = (0, 0)

class QQTMapElem2002(QQTMapElem):
    LifeTime = 1
    offset = (3, 12)
    imageID = 2002
    GridAttr = (0,)

class QQTMapElem4051(QQTMapElem):
    offset = (2, 41)
    imageID = 4051
    GridAttr = (0,)

class QQTMapElem2004(QQTMapElem):
    offset = (4, 25)
    imageID = 2004
    GridAttr = (0,)

class QQTMapElem2005(QQTMapElem):
    offset = (4, 25)
    imageID = 2005
    GridAttr = (0,)

class QQTMapElem2006(QQTMapElem):
    offset = (3, 19)
    imageID = 2006
    GridAttr = (0,)

class QQTMapElem2007(QQTMapElem):
    offset = (0, 25)
    imageID = 2007
    GridAttr = (0,)

class QQTMapElem2008(QQTMapElem):
    offset = (4, 36)
    size = (4, 2)
    imageID = 2008
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem17060(QQTMapElem):
    LifeTime = 1
    offset = (2, 11)
    imageID = 17060
    GridAttr = (0,)

class QQTMapElem4058(QQTMapElem):
    size = (1, 2)
    imageID = 4058
    GridAttr = (0, 0)

class QQTMapElem2011(QQTMapElem):
    offset = (4, 25)
    imageID = 2011
    GridAttr = (0,)

class QQTMapElem2012(QQTMapElem):
    LifeTime = 1
    canMove = 2
    canDoSpecial = 10
    offset = (2, 5)
    imageID = 2012
    GridAttr = (0,)

class QQTMapElem2014(QQTMapElem):
    offset = (3, 37)
    size = (4, 2)
    imageID = 2014
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem17061(QQTMapElem):
    offset = (-1, 69)
    size = (2, 1)
    imageID = 17061
    GridAttr = (0, 0)

class QQTMapElem2016(QQTMapElem):
    offset = (0, 23)
    imageID = 2016
    GridAttr = (0,)

class QQTMapElem2019(QQTMapElem):
    offset = (4, 27)
    imageID = 2019
    GridAttr = (0,)

class QQTMapElem17062(QQTMapElem):
    offset = (2, 34)
    imageID = 17062
    GridAttr = (0,)

class QQTMapElem4070(QQTMapElem):
    offset = (-1, 0)
    size = (12, 8)
    imageID = 4070
    GridAttr = (3855, 0, 3855, 3855, 3855, 3855, 3855, 3855, 0, 0, 3855, 3855, 3855, 3855, 3855, 3855, 0, 0, 3855, 3855, 3855, 3855, 3855, 3855, 0, 0, 3855, 3855, 3855, 3855, 3855, 3855, 0, 0, 0, 3855, 3855, 3855, 3855, 3855, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3855, 3855, 3855, 0, 0, 0, 0, 3855, 3855, 3855, 3855, 3855, 3855, 0, 0, 3855, 3855, 3855, 3855, 3855, 3855)

class QQTMapElem4071(QQTMapElem):
    offset = (1, 0)
    size = (11, 8)
    imageID = 4071
    GridAttr = (3855, 0, 3855, 3855, 3855, 3855, 3855, 3855, 0, 0, 0, 3855, 3840, 3855, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3855, 3855, 3855, 3855, 3855, 3855, 0, 0, 3855, 3855, 3855, 3855, 3855, 3855, 0, 0, 3855, 3855, 3855, 512, 3855, 3855, 0, 0, 3855, 3855, 3855, 3855, 3855, 3855, 0, 0, 3855, 3855, 3855, 3855, 3855, 0)

class QQTMapElem4072(QQTMapElem):
    offset = (-5, 27)
    size = (3, 2)
    imageID = 4072
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem15015(QQTMapElem):
    offset = (4, 10)
    imageID = 15015
    GridAttr = (0,)

class QQTMapElem4078(QQTMapElem):
    offset = (1, 15)
    size = (3, 4)
    imageID = 4078
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem4079(QQTMapElem):
    offset = (4, 1)
    size = (8, 3)
    imageID = 4079
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem4080(QQTMapElem):
    offset = (2, 8)
    size = (3, 4)
    imageID = 4080
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem4081(QQTMapElem):
    offset = (10, 1)
    size = (2, 3)
    imageID = 4081
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem4082(QQTMapElem):
    offset = (1, 7)
    size = (5, 2)
    imageID = 4082
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem4083(QQTMapElem):
    offset = (-2, 5)
    size = (5, 2)
    imageID = 4083
    GridAttr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

class QQTMapElem4084(QQTMapElem):
    offset = (8, 3)
    size = (2, 3)
    imageID = 4084
    GridAttr = (0, 0, 0, 0, 0, 0)

class QQTMapElem17065(QQTMapElem):
    offset = (4, 39)
    size = (2, 1)
    imageID = 17065
    GridAttr = (0, 0)

class QQTMapElem2040(QQTMapElem):
    offset = (1, 5)
    imageID = 2040
    GridAttr = (0,)

class QQTMapElem2041(QQTMapElem):
    offset = (0, 5)
    imageID = 2041
    GridAttr = (0,)

class QQTMapElem17066(QQTMapElem):
    offset = (-4, -2)
    size = (2, 2)
    imageID = 17066
    GridAttr = (0, 0, 0, 0)

class QQTMapElem2048(QQTMapElem):
    size = (2, 1)
    imageID = 2048
    GridAttr = (3855, 3855)

class QQTMapElem2049(QQTMapElem):
    size = (1, 2)
    imageID = 2049
    GridAttr = (3855, 3855)

class QQTMapElem15019(QQTMapElem):
    imageID = 15019
    GridAttr = (3855,)

class QQTMapElem18208(QQTMapElem):
    imageID = 18208
    GridAttr = (3855,)

class QQTMapElem10011(QQTMapElem):
    imageID = 10011
    GridAttr = (3855,)

class QQTMapElem15023(QQTMapElem):
    imageID = 15023
    GridAttr = (3855,)

class QQTMapElem18209(QQTMapElem):
    imageID = 18209
    GridAttr = (3855,)

class QQTMapElem18210(QQTMapElem):
    imageID = 18210
    GridAttr = (3855,)

class QQTMapElem18211(QQTMapElem):
    imageID = 18211
    GridAttr = (3855,)

class QQTMapElem18212(QQTMapElem):
    imageID = 18212
    GridAttr = (3855,)

class QQTMapElem14015(QQTMapElem):
    imageID = 14015
    GridAttr = (3855,)

class QQTMapElem14016(QQTMapElem):
    imageID = 14016
    GridAttr = (3855,)

class QQTMapElem2033(QQTMapElem):
    imageID = 2033
    GridAttr = (3855,)

class QQTMapElem18214(QQTMapElem):
    imageID = 18214
    GridAttr = (3855,)

class QQTMapElem13004(QQTMapElem):
    imageID = 13004
    GridAttr = (3855,)

class QQTMapElem13005(QQTMapElem):
    imageID = 13005
    GridAttr = (3855,)

class QQTMapElem18215(QQTMapElem):
    imageID = 18215
    GridAttr = (3855,)

class QQTMapElem13006(QQTMapElem):
    imageID = 13006
    GridAttr = (3855,)

class QQTMapElem13015(QQTMapElem):
    canMove = 16
    canDoSpecial = 6
    imageID = 13015
    GridAttr = (3855,)

class QQTMapElem18217(QQTMapElem):
    imageID = 18217
    GridAttr = (3855,)

class QQTMapElem4033(QQTMapElem):
    imageID = 4033
    GridAttr = (3855,)

class QQTMapElem2034(QQTMapElem):
    imageID = 2034
    GridAttr = (3855,)

class QQTMapElem18218(QQTMapElem):
    imageID = 18218
    GridAttr = (3855,)

class QQTMapElem12001(QQTMapElem):
    imageID = 12001
    GridAttr = (3855,)

class QQTMapElem18219(QQTMapElem):
    imageID = 18219
    GridAttr = (3855,)

class QQTMapElem16101(QQTMapElem):
    imageID = 16101
    GridAttr = (3855,)

class QQTMapElem12006(QQTMapElem):
    imageID = 12006
    GridAttr = (3855,)

class QQTMapElem18220(QQTMapElem):
    imageID = 18220
    GridAttr = (3855,)

class QQTMapElem12007(QQTMapElem):
    imageID = 12007
    GridAttr = (3855,)

class QQTMapElem18221(QQTMapElem):
    imageID = 18221
    GridAttr = (3855,)

class QQTMapElem17133(QQTMapElem):
    imageID = 17133
    GridAttr = (3855,)

class QQTMapElem17130(QQTMapElem):
    imageID = 17130
    GridAttr = (3855,)

class QQTMapElem17134(QQTMapElem):
    imageID = 17134
    GridAttr = (3855,)

class QQTMapElem17135(QQTMapElem):
    imageID = 17135
    GridAttr = (3855,)

class QQTMapElem17136(QQTMapElem):
    imageID = 17136
    GridAttr = (3855,)

class QQTMapElem18222(QQTMapElem):
    imageID = 18222
    GridAttr = (3855,)

class QQTMapElem17131(QQTMapElem):
    imageID = 17131
    GridAttr = (3855,)

class QQTMapElem1012(QQTMapElem):
    imageID = 1012
    GridAttr = (3855,)

class QQTMapElem16115(QQTMapElem):
    imageID = 16115
    GridAttr = (3855,)

class QQTMapElem2035(QQTMapElem):
    imageID = 2035
    GridAttr = (3855,)

class QQTMapElem16117(QQTMapElem):
    imageID = 16117
    GridAttr = (3855,)

class QQTMapElem17132(QQTMapElem):
    imageID = 17132
    GridAttr = (3855,)

class QQTMapElem11001(QQTMapElem):
    offset = (1, 0)
    imageID = 11001
    GridAttr = (3855,)

class QQTMapElem13051(QQTMapElem):
    imageID = 13051
    GridAttr = (3855,)

class QQTMapElem13052(QQTMapElem):
    imageID = 13052
    GridAttr = (3855,)

class QQTMapElem13053(QQTMapElem):
    imageID = 13053
    GridAttr = (3855,)

class QQTMapElem18206(QQTMapElem):
    imageID = 18206
    GridAttr = (3855,)

class QQTMapElem2036(QQTMapElem):
    imageID = 2036
    GridAttr = (3855,)

class QQTMapElem17137(QQTMapElem):
    imageID = 17137
    GridAttr = (3855,)

class QQTMapElem3059(QQTMapElem):
    imageID = 3059
    GridAttr = (3855,)

class QQTMapElem10001(QQTMapElem):
    imageID = 10001
    GridAttr = (3855,)

class QQTMapElem17001(QQTMapElem):
    imageID = 17001
    GridAttr = (3855,)

class QQTMapElem14102(QQTMapElem):
    imageID = 14102
    GridAttr = (3855,)

class QQTMapElem17030(QQTMapElem):
    imageID = 17030
    GridAttr = (3855,)

class QQTMapElem17033(QQTMapElem):
    imageID = 17033
    GridAttr = (3855,)

class QQTMapElem17037(QQTMapElem):
    imageID = 17037
    GridAttr = (3855,)

class QQTMapElem17038(QQTMapElem):
    imageID = 17038
    GridAttr = (3855,)

class QQTMapElem17040(QQTMapElem):
    canMove = 2
    imageID = 17040
    GridAttr = (3855,)

class QQTMapElem17045(QQTMapElem):
    imageID = 17045
    GridAttr = (3855,)

class QQTMapElem15001(QQTMapElem):
    imageID = 15001
    GridAttr = (3855,)

class QQTMapElem2001(QQTMapElem):
    imageID = 2001
    GridAttr = (3855,)

class QQTMapElem13001(QQTMapElem):
    imageID = 13001
    GridAttr = (3855,)

class QQTMapElem13002(QQTMapElem):
    imageID = 13002
    GridAttr = (3855,)

class QQTMapElem13003(QQTMapElem):
    imageID = 13003
    GridAttr = (3855,)

class QQTMapElem18213(QQTMapElem):
    imageID = 18213
    GridAttr = (3855,)

class QQTMapElem17121(QQTMapElem):
    imageID = 17121
    GridAttr = (3855,)

class QQTMapElem17122(QQTMapElem):
    imageID = 17122
    GridAttr = (3855,)

class QQTMapElem17123(QQTMapElem):
    imageID = 17123
    GridAttr = (3855,)

class QQTMapElem17124(QQTMapElem):
    imageID = 17124
    GridAttr = (3855,)

class QQTMapElem17125(QQTMapElem):
    imageID = 17125
    GridAttr = (3855,)

class QQTMapElem17126(QQTMapElem):
    imageID = 17126
    GridAttr = (3855,)

class QQTMapElem17127(QQTMapElem):
    imageID = 17127
    GridAttr = (3855,)

class QQTMapElem17128(QQTMapElem):
    imageID = 17128
    GridAttr = (3855,)

class QQTMapElem18216(QQTMapElem):
    imageID = 18216
    GridAttr = (3855,)

class QQTMapElem13047(QQTMapElem):
    imageID = 13047
    GridAttr = (3855,)

class QQTMapElem13048(QQTMapElem):
    imageID = 13048
    GridAttr = (3855,)

class QQTMapElem13049(QQTMapElem):
    imageID = 13049
    GridAttr = (3855,)

class QQTMapElem18223(QQTMapElem):
    imageID = 18223
    GridAttr = (3855,)

class QQTMapElem9001(QQTMapElem):
    imageID = 9001
    GridAttr = (3855,)

class QQTMapElem9002(QQTMapElem):
    imageID = 9002
    GridAttr = (3855,)

class QQTMapElem7001(QQTMapElem):
    imageID = 7001
    GridAttr = (3855,)

class QQTMapElem7002(QQTMapElem):
    imageID = 7002
    GridAttr = (3855,)

class QQTMapElem7012(QQTMapElem):
    imageID = 7012
    GridAttr = (3855,)

class QQTMapElem7013(QQTMapElem):
    imageID = 7013
    GridAttr = (3855,)

class QQTMapElem7014(QQTMapElem):
    imageID = 7014
    GridAttr = (3855,)

class QQTMapElem5001(QQTMapElem):
    imageID = 5001
    GridAttr = (3855,)

class QQTMapElem5019(QQTMapElem):
    imageID = 5019
    GridAttr = (3855,)

class QQTMapElem18201(QQTMapElem):
    imageID = 18201
    GridAttr = (3855,)

class QQTMapElem3001(QQTMapElem):
    imageID = 3001
    GridAttr = (3855,)

class QQTMapElem3002(QQTMapElem):
    imageID = 3002
    GridAttr = (3855,)

class QQTMapElem3003(QQTMapElem):
    imageID = 3003
    GridAttr = (3855,)

class QQTMapElem1001(QQTMapElem):
    imageID = 1001
    GridAttr = (3855,)

class QQTMapElem2039(QQTMapElem):
    imageID = 2039
    GridAttr = (3855,)

class QQTMapElem1142(QQTMapElem):
    imageID = 1142
    GridAttr = (3855,)

class QQTMapElem1143(QQTMapElem):
    size = (5, 2)
    imageID = 1143
    GridAttr = (3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855)

class QQTMapElem18202(QQTMapElem):
    imageID = 18202
    GridAttr = (3855,)

class QQTMapElem6001(QQTMapElem):
    imageID = 6001
    GridAttr = (3855,)

class QQTMapElem6019(QQTMapElem):
    imageID = 6019
    GridAttr = (3855,)

class QQTMapElem6020(QQTMapElem):
    imageID = 6020
    GridAttr = (3855,)

class QQTMapElem17071(QQTMapElem):
    offset = (0, 6)
    size = (3, 1)
    imageID = 17071
    GridAttr = (3855, 3855, 3855)

class QQTMapElem6022(QQTMapElem):
    imageID = 6022
    GridAttr = (3855,)

class QQTMapElem18207(QQTMapElem):
    imageID = 18207
    GridAttr = (3855,)

class QQTMapElem4001(QQTMapElem):
    imageID = 4001
    GridAttr = (3855,)

class QQTMapElem2027(QQTMapElem):
    size = (1, 2)
    imageID = 2027
    GridAttr = (3855, 3855)

class QQTMapElem4003(QQTMapElem):
    imageID = 4003
    GridAttr = (3855,)

class QQTMapElem4009(QQTMapElem):
    imageID = 4009
    GridAttr = (3855,)

class QQTMapElem16118(QQTMapElem):
    imageID = 16118
    GridAttr = (3855,)

class QQTMapElem2030(QQTMapElem):
    imageID = 2030
    GridAttr = (3855,)

class QQTMapElem14101(QQTMapElem):
    imageID = 14101
    GridAttr = (3855,)

class QQTMapElem18205(QQTMapElem):
    imageID = 18205
    GridAttr = (3855,)

class QQTMapElem2031(QQTMapElem):
    imageID = 2031
    GridAttr = (3855,)

class QQTMapElem10010(QQTMapElem):
    imageID = 10010
    GridAttr = (3855,)

class QQTMapElem3006(QQTMapElem):
    size = (3, 2)
    imageID = 3006
    GridAttr = (3855, 3855, 3855, 3855, 3855, 3855)

class QQTMapElem16010(QQTMapElem):
    imageID = 16010
    GridAttr = (3855,)

class QQTMapElem4039(QQTMapElem):
    imageID = 4039
    GridAttr = (3855,)

class QQTMapElem14001(QQTMapElem):
    imageID = 14001
    GridAttr = (3855,)

class QQTMapElem14002(QQTMapElem):
    imageID = 14002
    GridAttr = (3855,)

class QQTMapElem14003(QQTMapElem):
    imageID = 14003
    GridAttr = (3855,)

class QQTMapElem14004(QQTMapElem):
    imageID = 14004
    GridAttr = (3855,)

class QQTMapElem14017(QQTMapElem):
    imageID = 14017
    GridAttr = (3855,)

class QQTMapElem14034(QQTMapElem):
    imageID = 14034
    GridAttr = (3855,)

class QQTMapElem14035(QQTMapElem):
    imageID = 14035
    GridAttr = (3855,)

class QQTMapElem14037(QQTMapElem):
    imageID = 14037
    GridAttr = (3855,)

class QQTMapElem12005(QQTMapElem):
    imageID = 12005
    GridAttr = (3855,)

class QQTMapElem12022(QQTMapElem):
    size = (5, 2)
    imageID = 12022
    GridAttr = (3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855)

class QQTMapElem16119(QQTMapElem):
    imageID = 16119
    GridAttr = (3855,)

class QQTMapElem16120(QQTMapElem):
    imageID = 16120
    GridAttr = (3855,)

class QQTMapElem16122(QQTMapElem):
    imageID = 16122
    GridAttr = (3855,)

class QQTMapElem4056(QQTMapElem):
    imageID = 4056
    GridAttr = (3855,)

class QQTMapElem18224(QQTMapElem):
    imageID = 18224
    GridAttr = (3855,)

class QQTMapElem18225(QQTMapElem):
    imageID = 18225
    GridAttr = (3855,)

class QQTMapElem18226(QQTMapElem):
    imageID = 18226
    GridAttr = (3855,)

class QQTMapElem18227(QQTMapElem):
    imageID = 18227
    GridAttr = (3855,)

class QQTMapElem18228(QQTMapElem):
    imageID = 18228
    GridAttr = (3855,)

class QQTMapElem8011(QQTMapElem):
    imageID = 8011
    GridAttr = (3855,)

class QQTMapElem8013(QQTMapElem):
    imageID = 8013
    GridAttr = (3855,)

class QQTMapElem8015(QQTMapElem):
    imageID = 8015
    GridAttr = (3855,)

class QQTMapElem8016(QQTMapElem):
    offset = (0, -5)
    imageID = 8016
    GridAttr = (3855,)

class QQTMapElem8017(QQTMapElem):
    imageID = 8017
    GridAttr = (3855,)

class QQTMapElem8024(QQTMapElem):
    size = (5, 4)
    imageID = 8024
    GridAttr = (3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855)

class QQTMapElem8025(QQTMapElem):
    size = (5, 2)
    imageID = 8025
    GridAttr = (3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855)

class QQTMapElem8026(QQTMapElem):
    size = (3, 3)
    imageID = 8026
    GridAttr = (3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855)

class QQTMapElem8027(QQTMapElem):
    size = (4, 3)
    imageID = 8027
    GridAttr = (3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855)

class QQTMapElem8028(QQTMapElem):
    size = (5, 2)
    imageID = 8028
    GridAttr = (3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855, 3855)

class QQTMapElem2021(QQTMapElem):
    size = (2, 2)
    imageID = 2021
    GridAttr = (3855, 3855, 3855, 3855)

class QQTMapElem2022(QQTMapElem):
    size = (2, 2)
    imageID = 2022
    GridAttr = (3855, 3855, 3855, 3855)

class QQTMapElem18203(QQTMapElem):
    size = (2, 2)
    imageID = 18203
    GridAttr = (3855, 3855, 3855, 3855)

class QQTMapElem2023(QQTMapElem):
    size = (2, 2)
    imageID = 2023
    GridAttr = (3855, 3855, 3855, 3855)

class QQTMapElem2024(QQTMapElem):
    imageID = 2024
    GridAttr = (3855,)

class QQTMapElem6017(QQTMapElem):
    imageID = 6017
    GridAttr = (3855,)

class QQTMapElem6018(QQTMapElem):
    imageID = 6018
    GridAttr = (3855,)

class QQTMapElem16121(QQTMapElem):
    imageID = 16121
    GridAttr = (3855,)

class QQTMapElem6021(QQTMapElem):
    imageID = 6021
    GridAttr = (3855,)

class QQTMapElem18204(QQTMapElem):
    imageID = 18204
    GridAttr = (3855,)

class QQTMapElem6023(QQTMapElem):
    imageID = 6023
    GridAttr = (3855,)

class QQTMapElem6024(QQTMapElem):
    imageID = 6024
    GridAttr = (3855,)

class QQTMapElem2032(QQTMapElem):
    imageID = 2032
    GridAttr = (3855,)

class QQTMapElem3053(QQTMapElem):
    imageID = 3053
    GridAttr = (3855,)

class QQTMapElem2045(QQTMapElem):
    size = (2, 2)
    imageID = 2045
    GridAttr = (3855, 3855, 3855, 3855)

class QQTMapElem4002(QQTMapElem):
    imageID = 4002
    GridAttr = (3855,)

class QQTMapElem4010(QQTMapElem):
    imageID = 4010
    GridAttr = (3855,)

class QQTMapElem4011(QQTMapElem):
    imageID = 4011
    GridAttr = (3855,)

class QQTMapElem4030(QQTMapElem):
    imageID = 4030
    GridAttr = (3855,)

class QQTMapElem4031(QQTMapElem):
    imageID = 4031
    GridAttr = (3855,)

class QQTMapElem4032(QQTMapElem):
    imageID = 4032
    GridAttr = (3855,)

class QQTMapElem4034(QQTMapElem):
    imageID = 4034
    GridAttr = (3855,)

class QQTMapElem4035(QQTMapElem):
    imageID = 4035
    GridAttr = (3855,)

class QQTMapElem4036(QQTMapElem):
    imageID = 4036
    GridAttr = (3855,)

class QQTMapElem4037(QQTMapElem):
    imageID = 4037
    GridAttr = (3855,)

class QQTMapElem4038(QQTMapElem):
    imageID = 4038
    GridAttr = (3855,)

class QQTMapElem2013(QQTMapElem):
    imageID = 2013
    GridAttr = (3855,)

class QQTMapElem2017(QQTMapElem):
    imageID = 2017
    GridAttr = (3855,)

class QQTMapElem2018(QQTMapElem):
    imageID = 2018
    GridAttr = (3855,)

class QQTMapElem2020(QQTMapElem):
    size = (2, 2)
    imageID = 2020
    GridAttr = (3855, 3855, 3855, 3855)

class QQTMapElem2025(QQTMapElem):
    imageID = 2025
    GridAttr = (3855,)

class QQTMapElem2026(QQTMapElem):
    size = (2, 1)
    imageID = 2026
    GridAttr = (3855, 3855)

class QQTMapElem2028(QQTMapElem):
    imageID = 2028
    GridAttr = (3855,)

class QQTMapElem2029(QQTMapElem):
    imageID = 2029
    GridAttr = (3855,)

class QQTMapElem2037(QQTMapElem):
    imageID = 2037
    GridAttr = (3855,)

class QQTMapElem2038(QQTMapElem):
    size = (2, 2)
    imageID = 2038
    GridAttr = (3855, 3855, 3855, 3855)

class QQTMapElem2042(QQTMapElem):
    size = (2, 2)
    imageID = 2042
    GridAttr = (3855, 3855, 3855, 3855)

class QQTMapElem2043(QQTMapElem):
    size = (2, 2)
    imageID = 2043
    GridAttr = (3855, 3855, 3855, 3855)

class QQTMapElem2044(QQTMapElem):
    size = (2, 2)
    imageID = 2044
    GridAttr = (3855, 3855, 3855, 3855)

class QQTMapElem2046(QQTMapElem):
    imageID = 2046
    GridAttr = (3855,)

class QQTMapElem2047(QQTMapElem):
    imageID = 2047
    GridAttr = (3855,)

class QQTMapElem17026(QQTMapElem):
    offset = (6, 7)
    imageID = 17026
    GridAttr = (3855,)

class QQTMapElem17029(QQTMapElem):
    offset = (5, 7)
    imageID = 17029
    GridAttr = (3855,)

qqtMapElems = {
    15020:QQTMapElem15020,
    15021:QQTMapElem15021,
    14007:QQTMapElem14007,
    14010:QQTMapElem14010,
    14012:QQTMapElem14012,
    17053:QQTMapElem17053,
    17055:QQTMapElem17055,
    13007:QQTMapElem13007,
    13008:QQTMapElem13008,
    17105:QQTMapElem17105,
    13010:QQTMapElem13010,
    17107:QQTMapElem17107,
    17108:QQTMapElem17108,
    17109:QQTMapElem17109,
    17110:QQTMapElem17110,
    17112:QQTMapElem17112,
    17113:QQTMapElem17113,
    17059:QQTMapElem17059,
    12008:QQTMapElem12008,
    16105:QQTMapElem16105,
    12010:QQTMapElem12010,
    16107:QQTMapElem16107,
    12012:QQTMapElem12012,
    16116:QQTMapElem16116,
    17064:QQTMapElem17064,
    11002:QQTMapElem11002,
    11006:QQTMapElem11006,
    13055:QQTMapElem13055,
    13056:QQTMapElem13056,
    13057:QQTMapElem13057,
    10004:QQTMapElem10004,
    17018:QQTMapElem17018,
    17019:QQTMapElem17019,
    17021:QQTMapElem17021,
    17022:QQTMapElem17022,
    17023:QQTMapElem17023,
    17024:QQTMapElem17024,
    17025:QQTMapElem17025,
    17027:QQTMapElem17027,
    17028:QQTMapElem17028,
    4045:QQTMapElem4045,
    14103:QQTMapElem14103,
    17039:QQTMapElem17039,
    10008:QQTMapElem10008,
    17046:QQTMapElem17046,
    17047:QQTMapElem17047,
    17048:QQTMapElem17048,
    17050:QQTMapElem17050,
    15003:QQTMapElem15003,
    15004:QQTMapElem15004,
    15005:QQTMapElem15005,
    17054:QQTMapElem17054,
    15007:QQTMapElem15007,
    17056:QQTMapElem17056,
    15009:QQTMapElem15009,
    15010:QQTMapElem15010,
    15011:QQTMapElem15011,
    15012:QQTMapElem15012,
    15013:QQTMapElem15013,
    15014:QQTMapElem15014,
    17063:QQTMapElem17063,
    15016:QQTMapElem15016,
    15017:QQTMapElem15017,
    15018:QQTMapElem15018,
    17067:QQTMapElem17067,
    17068:QQTMapElem17068,
    17069:QQTMapElem17069,
    17070:QQTMapElem17070,
    10013:QQTMapElem10013,
    17072:QQTMapElem17072,
    17073:QQTMapElem17073,
    17074:QQTMapElem17074,
    17075:QQTMapElem17075,
    17076:QQTMapElem17076,
    17077:QQTMapElem17077,
    17078:QQTMapElem17078,
    17079:QQTMapElem17079,
    17080:QQTMapElem17080,
    17081:QQTMapElem17081,
    17082:QQTMapElem17082,
    17083:QQTMapElem17083,
    10016:QQTMapElem10016,
    14113:QQTMapElem14113,
    17100:QQTMapElem17100,
    17101:QQTMapElem17101,
    17102:QQTMapElem17102,
    17103:QQTMapElem17103,
    17104:QQTMapElem17104,
    13009:QQTMapElem13009,
    17106:QQTMapElem17106,
    13011:QQTMapElem13011,
    13012:QQTMapElem13012,
    13013:QQTMapElem13013,
    13014:QQTMapElem13014,
    17111:QQTMapElem17111,
    13016:QQTMapElem13016,
    13017:QQTMapElem13017,
    17114:QQTMapElem17114,
    17115:QQTMapElem17115,
    13020:QQTMapElem13020,
    13021:QQTMapElem13021,
    13022:QQTMapElem13022,
    13024:QQTMapElem13024,
    13034:QQTMapElem13034,
    13035:QQTMapElem13035,
    13036:QQTMapElem13036,
    13037:QQTMapElem13037,
    13038:QQTMapElem13038,
    13039:QQTMapElem13039,
    13040:QQTMapElem13040,
    13042:QQTMapElem13042,
    13043:QQTMapElem13043,
    13044:QQTMapElem13044,
    13045:QQTMapElem13045,
    13046:QQTMapElem13046,
    13050:QQTMapElem13050,
    11003:QQTMapElem11003,
    11004:QQTMapElem11004,
    11005:QQTMapElem11005,
    13054:QQTMapElem13054,
    11007:QQTMapElem11007,
    11008:QQTMapElem11008,
    11009:QQTMapElem11009,
    13058:QQTMapElem13058,
    13059:QQTMapElem13059,
    13060:QQTMapElem13060,
    13061:QQTMapElem13061,
    13062:QQTMapElem13062,
    13063:QQTMapElem13063,
    13064:QQTMapElem13064,
    13065:QQTMapElem13065,
    13066:QQTMapElem13066,
    13067:QQTMapElem13067,
    13068:QQTMapElem13068,
    13069:QQTMapElem13069,
    13070:QQTMapElem13070,
    13071:QQTMapElem13071,
    13072:QQTMapElem13072,
    13073:QQTMapElem13073,
    13074:QQTMapElem13074,
    13075:QQTMapElem13075,
    13076:QQTMapElem13076,
    13077:QQTMapElem13077,
    13078:QQTMapElem13078,
    13079:QQTMapElem13079,
    4050:QQTMapElem4050,
    9003:QQTMapElem9003,
    9004:QQTMapElem9004,
    9005:QQTMapElem9005,
    9006:QQTMapElem9006,
    9007:QQTMapElem9007,
    9008:QQTMapElem9008,
    9009:QQTMapElem9009,
    9010:QQTMapElem9010,
    9011:QQTMapElem9011,
    9012:QQTMapElem9012,
    9013:QQTMapElem9013,
    9014:QQTMapElem9014,
    7003:QQTMapElem7003,
    7004:QQTMapElem7004,
    7005:QQTMapElem7005,
    7006:QQTMapElem7006,
    7007:QQTMapElem7007,
    7008:QQTMapElem7008,
    7010:QQTMapElem7010,
    7011:QQTMapElem7011,
    18241:QQTMapElem18241,
    5002:QQTMapElem5002,
    5003:QQTMapElem5003,
    5004:QQTMapElem5004,
    5005:QQTMapElem5005,
    5006:QQTMapElem5006,
    5007:QQTMapElem5007,
    5008:QQTMapElem5008,
    5009:QQTMapElem5009,
    5010:QQTMapElem5010,
    5011:QQTMapElem5011,
    5012:QQTMapElem5012,
    5013:QQTMapElem5013,
    5014:QQTMapElem5014,
    5015:QQTMapElem5015,
    5016:QQTMapElem5016,
    5017:QQTMapElem5017,
    5018:QQTMapElem5018,
    5020:QQTMapElem5020,
    5021:QQTMapElem5021,
    5023:QQTMapElem5023,
    5024:QQTMapElem5024,
    5025:QQTMapElem5025,
    5026:QQTMapElem5026,
    5028:QQTMapElem5028,
    5029:QQTMapElem5029,
    5030:QQTMapElem5030,
    5034:QQTMapElem5034,
    5035:QQTMapElem5035,
    5036:QQTMapElem5036,
    5037:QQTMapElem5037,
    3004:QQTMapElem3004,
    3005:QQTMapElem3005,
    4057:QQTMapElem4057,
    3007:QQTMapElem3007,
    3008:QQTMapElem3008,
    3009:QQTMapElem3009,
    3010:QQTMapElem3010,
    3011:QQTMapElem3011,
    3012:QQTMapElem3012,
    3013:QQTMapElem3013,
    3014:QQTMapElem3014,
    3015:QQTMapElem3015,
    3017:QQTMapElem3017,
    3018:QQTMapElem3018,
    3019:QQTMapElem3019,
    3020:QQTMapElem3020,
    3022:QQTMapElem3022,
    3023:QQTMapElem3023,
    3024:QQTMapElem3024,
    3025:QQTMapElem3025,
    3026:QQTMapElem3026,
    3050:QQTMapElem3050,
    1003:QQTMapElem1003,
    1004:QQTMapElem1004,
    1005:QQTMapElem1005,
    1006:QQTMapElem1006,
    1007:QQTMapElem1007,
    1008:QQTMapElem1008,
    1009:QQTMapElem1009,
    3058:QQTMapElem3058,
    1011:QQTMapElem1011,
    3060:QQTMapElem3060,
    3061:QQTMapElem3061,
    18242:QQTMapElem18242,
    4059:QQTMapElem4059,
    3120:QQTMapElem3120,
    3121:QQTMapElem3121,
    3122:QQTMapElem3122,
    4060:QQTMapElem4060,
    14110:QQTMapElem14110,
    1113:QQTMapElem1113,
    1114:QQTMapElem1114,
    1115:QQTMapElem1115,
    1116:QQTMapElem1116,
    1117:QQTMapElem1117,
    1118:QQTMapElem1118,
    1119:QQTMapElem1119,
    1120:QQTMapElem1120,
    1121:QQTMapElem1121,
    1122:QQTMapElem1122,
    1123:QQTMapElem1123,
    1124:QQTMapElem1124,
    1125:QQTMapElem1125,
    1126:QQTMapElem1126,
    1127:QQTMapElem1127,
    1128:QQTMapElem1128,
    1129:QQTMapElem1129,
    1130:QQTMapElem1130,
    1131:QQTMapElem1131,
    1132:QQTMapElem1132,
    1133:QQTMapElem1133,
    1134:QQTMapElem1134,
    1135:QQTMapElem1135,
    1136:QQTMapElem1136,
    1137:QQTMapElem1137,
    1138:QQTMapElem1138,
    1139:QQTMapElem1139,
    1140:QQTMapElem1140,
    1141:QQTMapElem1141,
    6013:QQTMapElem6013,
    4007:QQTMapElem4007,
    2015:QQTMapElem2015,
    4013:QQTMapElem4013,
    10009:QQTMapElem10009,
    4021:QQTMapElem4021,
    18002:QQTMapElem18002,
    18003:QQTMapElem18003,
    18004:QQTMapElem18004,
    18005:QQTMapElem18005,
    18006:QQTMapElem18006,
    18007:QQTMapElem18007,
    18008:QQTMapElem18008,
    18009:QQTMapElem18009,
    18020:QQTMapElem18020,
    18021:QQTMapElem18021,
    18022:QQTMapElem18022,
    18023:QQTMapElem18023,
    18024:QQTMapElem18024,
    18025:QQTMapElem18025,
    18026:QQTMapElem18026,
    18027:QQTMapElem18027,
    18028:QQTMapElem18028,
    16001:QQTMapElem16001,
    16002:QQTMapElem16002,
    16003:QQTMapElem16003,
    16004:QQTMapElem16004,
    16005:QQTMapElem16005,
    16006:QQTMapElem16006,
    16007:QQTMapElem16007,
    16008:QQTMapElem16008,
    16009:QQTMapElem16009,
    16011:QQTMapElem16011,
    16012:QQTMapElem16012,
    16013:QQTMapElem16013,
    16014:QQTMapElem16014,
    16015:QQTMapElem16015,
    16016:QQTMapElem16016,
    16017:QQTMapElem16017,
    16018:QQTMapElem16018,
    16019:QQTMapElem16019,
    16020:QQTMapElem16020,
    16021:QQTMapElem16021,
    16022:QQTMapElem16022,
    16023:QQTMapElem16023,
    16024:QQTMapElem16024,
    16025:QQTMapElem16025,
    16026:QQTMapElem16026,
    16027:QQTMapElem16027,
    16028:QQTMapElem16028,
    16029:QQTMapElem16029,
    16030:QQTMapElem16030,
    16031:QQTMapElem16031,
    16032:QQTMapElem16032,
    16033:QQTMapElem16033,
    16034:QQTMapElem16034,
    16035:QQTMapElem16035,
    16036:QQTMapElem16036,
    16037:QQTMapElem16037,
    16038:QQTMapElem16038,
    18101:QQTMapElem18101,
    18102:QQTMapElem18102,
    18103:QQTMapElem18103,
    18104:QQTMapElem18104,
    18105:QQTMapElem18105,
    18106:QQTMapElem18106,
    18107:QQTMapElem18107,
    18108:QQTMapElem18108,
    18109:QQTMapElem18109,
    18111:QQTMapElem18111,
    18112:QQTMapElem18112,
    14022:QQTMapElem14022,
    14023:QQTMapElem14023,
    14024:QQTMapElem14024,
    14025:QQTMapElem14025,
    14026:QQTMapElem14026,
    14027:QQTMapElem14027,
    14028:QQTMapElem14028,
    14029:QQTMapElem14029,
    14030:QQTMapElem14030,
    14031:QQTMapElem14031,
    14032:QQTMapElem14032,
    14033:QQTMapElem14033,
    14036:QQTMapElem14036,
    14038:QQTMapElem14038,
    14039:QQTMapElem14039,
    14040:QQTMapElem14040,
    14041:QQTMapElem14041,
    14042:QQTMapElem14042,
    14043:QQTMapElem14043,
    14044:QQTMapElem14044,
    14045:QQTMapElem14045,
    14046:QQTMapElem14046,
    14047:QQTMapElem14047,
    14048:QQTMapElem14048,
    14049:QQTMapElem14049,
    12002:QQTMapElem12002,
    12003:QQTMapElem12003,
    12004:QQTMapElem12004,
    16102:QQTMapElem16102,
    16103:QQTMapElem16103,
    16104:QQTMapElem16104,
    12009:QQTMapElem12009,
    16106:QQTMapElem16106,
    12011:QQTMapElem12011,
    16108:QQTMapElem16108,
    16109:QQTMapElem16109,
    16110:QQTMapElem16110,
    16111:QQTMapElem16111,
    16112:QQTMapElem16112,
    16113:QQTMapElem16113,
    16114:QQTMapElem16114,
    2003:QQTMapElem2003,
    12020:QQTMapElem12020,
    12021:QQTMapElem12021,
    4052:QQTMapElem4052,
    4053:QQTMapElem4053,
    4054:QQTMapElem4054,
    14108:QQTMapElem14108,
    4055:QQTMapElem4055,
    10002:QQTMapElem10002,
    10003:QQTMapElem10003,
    14100:QQTMapElem14100,
    10005:QQTMapElem10005,
    10006:QQTMapElem10006,
    10007:QQTMapElem10007,
    14104:QQTMapElem14104,
    14105:QQTMapElem14105,
    14106:QQTMapElem14106,
    14107:QQTMapElem14107,
    10012:QQTMapElem10012,
    14109:QQTMapElem14109,
    10014:QQTMapElem10014,
    10015:QQTMapElem10015,
    14112:QQTMapElem14112,
    10017:QQTMapElem10017,
    14114:QQTMapElem14114,
    14115:QQTMapElem14115,
    14116:QQTMapElem14116,
    14117:QQTMapElem14117,
    14118:QQTMapElem14118,
    14119:QQTMapElem14119,
    14120:QQTMapElem14120,
    14121:QQTMapElem14121,
    14122:QQTMapElem14122,
    14123:QQTMapElem14123,
    14124:QQTMapElem14124,
    14125:QQTMapElem14125,
    14126:QQTMapElem14126,
    14127:QQTMapElem14127,
    18229:QQTMapElem18229,
    18230:QQTMapElem18230,
    18231:QQTMapElem18231,
    18232:QQTMapElem18232,
    18233:QQTMapElem18233,
    18234:QQTMapElem18234,
    18235:QQTMapElem18235,
    18236:QQTMapElem18236,
    18237:QQTMapElem18237,
    18238:QQTMapElem18238,
    18239:QQTMapElem18239,
    18240:QQTMapElem18240,
    8001:QQTMapElem8001,
    8002:QQTMapElem8002,
    8003:QQTMapElem8003,
    8004:QQTMapElem8004,
    8005:QQTMapElem8005,
    8006:QQTMapElem8006,
    8007:QQTMapElem8007,
    8008:QQTMapElem8008,
    8009:QQTMapElem8009,
    8010:QQTMapElem8010,
    8012:QQTMapElem8012,
    8014:QQTMapElem8014,
    8018:QQTMapElem8018,
    8019:QQTMapElem8019,
    8021:QQTMapElem8021,
    8022:QQTMapElem8022,
    8023:QQTMapElem8023,
    14111:QQTMapElem14111,
    6002:QQTMapElem6002,
    6003:QQTMapElem6003,
    6004:QQTMapElem6004,
    6005:QQTMapElem6005,
    6006:QQTMapElem6006,
    6007:QQTMapElem6007,
    6008:QQTMapElem6008,
    6009:QQTMapElem6009,
    6010:QQTMapElem6010,
    6011:QQTMapElem6011,
    6012:QQTMapElem6012,
    1002:QQTMapElem1002,
    6014:QQTMapElem6014,
    6015:QQTMapElem6015,
    6016:QQTMapElem6016,
    3051:QQTMapElem3051,
    3054:QQTMapElem3054,
    3055:QQTMapElem3055,
    15002:QQTMapElem15002,
    3056:QQTMapElem3056,
    17051:QQTMapElem17051,
    4004:QQTMapElem4004,
    4005:QQTMapElem4005,
    4006:QQTMapElem4006,
    3057:QQTMapElem3057,
    4008:QQTMapElem4008,
    17052:QQTMapElem17052,
    4012:QQTMapElem4012,
    1010:QQTMapElem1010,
    4014:QQTMapElem4014,
    4015:QQTMapElem4015,
    4016:QQTMapElem4016,
    4017:QQTMapElem4017,
    4018:QQTMapElem4018,
    4019:QQTMapElem4019,
    4020:QQTMapElem4020,
    15006:QQTMapElem15006,
    4022:QQTMapElem4022,
    4023:QQTMapElem4023,
    4024:QQTMapElem4024,
    4025:QQTMapElem4025,
    4026:QQTMapElem4026,
    4027:QQTMapElem4027,
    4028:QQTMapElem4028,
    4029:QQTMapElem4029,
    15008:QQTMapElem15008,
    17057:QQTMapElem17057,
    4040:QQTMapElem4040,
    4041:QQTMapElem4041,
    4042:QQTMapElem4042,
    4043:QQTMapElem4043,
    4044:QQTMapElem4044,
    17058:QQTMapElem17058,
    4046:QQTMapElem4046,
    4047:QQTMapElem4047,
    4048:QQTMapElem4048,
    4049:QQTMapElem4049,
    2002:QQTMapElem2002,
    4051:QQTMapElem4051,
    2004:QQTMapElem2004,
    2005:QQTMapElem2005,
    2006:QQTMapElem2006,
    2007:QQTMapElem2007,
    2008:QQTMapElem2008,
    17060:QQTMapElem17060,
    4058:QQTMapElem4058,
    2011:QQTMapElem2011,
    2012:QQTMapElem2012,
    2014:QQTMapElem2014,
    17061:QQTMapElem17061,
    2016:QQTMapElem2016,
    2019:QQTMapElem2019,
    17062:QQTMapElem17062,
    4070:QQTMapElem4070,
    4071:QQTMapElem4071,
    4072:QQTMapElem4072,
    15015:QQTMapElem15015,
    4078:QQTMapElem4078,
    4079:QQTMapElem4079,
    4080:QQTMapElem4080,
    4081:QQTMapElem4081,
    4082:QQTMapElem4082,
    4083:QQTMapElem4083,
    4084:QQTMapElem4084,
    17065:QQTMapElem17065,
    2040:QQTMapElem2040,
    2041:QQTMapElem2041,
    17066:QQTMapElem17066,
    2048:QQTMapElem2048,
    2049:QQTMapElem2049,
    15019:QQTMapElem15019,
    18208:QQTMapElem18208,
    10011:QQTMapElem10011,
    15023:QQTMapElem15023,
    18209:QQTMapElem18209,
    18210:QQTMapElem18210,
    18211:QQTMapElem18211,
    18212:QQTMapElem18212,
    14015:QQTMapElem14015,
    14016:QQTMapElem14016,
    2033:QQTMapElem2033,
    18214:QQTMapElem18214,
    13004:QQTMapElem13004,
    13005:QQTMapElem13005,
    18215:QQTMapElem18215,
    13006:QQTMapElem13006,
    13015:QQTMapElem13015,
    18217:QQTMapElem18217,
    4033:QQTMapElem4033,
    2034:QQTMapElem2034,
    18218:QQTMapElem18218,
    12001:QQTMapElem12001,
    18219:QQTMapElem18219,
    16101:QQTMapElem16101,
    12006:QQTMapElem12006,
    18220:QQTMapElem18220,
    12007:QQTMapElem12007,
    18221:QQTMapElem18221,
    17133:QQTMapElem17133,
    17130:QQTMapElem17130,
    17134:QQTMapElem17134,
    17135:QQTMapElem17135,
    17136:QQTMapElem17136,
    18222:QQTMapElem18222,
    17131:QQTMapElem17131,
    1012:QQTMapElem1012,
    16115:QQTMapElem16115,
    2035:QQTMapElem2035,
    16117:QQTMapElem16117,
    17132:QQTMapElem17132,
    11001:QQTMapElem11001,
    13051:QQTMapElem13051,
    13052:QQTMapElem13052,
    13053:QQTMapElem13053,
    18206:QQTMapElem18206,
    2036:QQTMapElem2036,
    17137:QQTMapElem17137,
    3059:QQTMapElem3059,
    10001:QQTMapElem10001,
    17001:QQTMapElem17001,
    14102:QQTMapElem14102,
    17030:QQTMapElem17030,
    17033:QQTMapElem17033,
    17037:QQTMapElem17037,
    17038:QQTMapElem17038,
    17040:QQTMapElem17040,
    17045:QQTMapElem17045,
    15001:QQTMapElem15001,
    2001:QQTMapElem2001,
    13001:QQTMapElem13001,
    13002:QQTMapElem13002,
    13003:QQTMapElem13003,
    18213:QQTMapElem18213,
    17121:QQTMapElem17121,
    17122:QQTMapElem17122,
    17123:QQTMapElem17123,
    17124:QQTMapElem17124,
    17125:QQTMapElem17125,
    17126:QQTMapElem17126,
    17127:QQTMapElem17127,
    17128:QQTMapElem17128,
    18216:QQTMapElem18216,
    13047:QQTMapElem13047,
    13048:QQTMapElem13048,
    13049:QQTMapElem13049,
    18223:QQTMapElem18223,
    9001:QQTMapElem9001,
    9002:QQTMapElem9002,
    7001:QQTMapElem7001,
    7002:QQTMapElem7002,
    7012:QQTMapElem7012,
    7013:QQTMapElem7013,
    7014:QQTMapElem7014,
    5001:QQTMapElem5001,
    5019:QQTMapElem5019,
    18201:QQTMapElem18201,
    3001:QQTMapElem3001,
    3002:QQTMapElem3002,
    3003:QQTMapElem3003,
    1001:QQTMapElem1001,
    2039:QQTMapElem2039,
    1142:QQTMapElem1142,
    1143:QQTMapElem1143,
    18202:QQTMapElem18202,
    6001:QQTMapElem6001,
    6019:QQTMapElem6019,
    6020:QQTMapElem6020,
    17071:QQTMapElem17071,
    6022:QQTMapElem6022,
    18207:QQTMapElem18207,
    4001:QQTMapElem4001,
    2027:QQTMapElem2027,
    4003:QQTMapElem4003,
    4009:QQTMapElem4009,
    16118:QQTMapElem16118,
    2030:QQTMapElem2030,
    14101:QQTMapElem14101,
    18205:QQTMapElem18205,
    2031:QQTMapElem2031,
    10010:QQTMapElem10010,
    3006:QQTMapElem3006,
    16010:QQTMapElem16010,
    4039:QQTMapElem4039,
    14001:QQTMapElem14001,
    14002:QQTMapElem14002,
    14003:QQTMapElem14003,
    14004:QQTMapElem14004,
    14017:QQTMapElem14017,
    14034:QQTMapElem14034,
    14035:QQTMapElem14035,
    14037:QQTMapElem14037,
    12005:QQTMapElem12005,
    12022:QQTMapElem12022,
    16119:QQTMapElem16119,
    16120:QQTMapElem16120,
    16122:QQTMapElem16122,
    4056:QQTMapElem4056,
    18224:QQTMapElem18224,
    18225:QQTMapElem18225,
    18226:QQTMapElem18226,
    18227:QQTMapElem18227,
    18228:QQTMapElem18228,
    8011:QQTMapElem8011,
    8013:QQTMapElem8013,
    8015:QQTMapElem8015,
    8016:QQTMapElem8016,
    8017:QQTMapElem8017,
    8024:QQTMapElem8024,
    8025:QQTMapElem8025,
    8026:QQTMapElem8026,
    8027:QQTMapElem8027,
    8028:QQTMapElem8028,
    2021:QQTMapElem2021,
    2022:QQTMapElem2022,
    18203:QQTMapElem18203,
    2023:QQTMapElem2023,
    2024:QQTMapElem2024,
    6017:QQTMapElem6017,
    6018:QQTMapElem6018,
    16121:QQTMapElem16121,
    6021:QQTMapElem6021,
    18204:QQTMapElem18204,
    6023:QQTMapElem6023,
    6024:QQTMapElem6024,
    2032:QQTMapElem2032,
    3053:QQTMapElem3053,
    2045:QQTMapElem2045,
    4002:QQTMapElem4002,
    4010:QQTMapElem4010,
    4011:QQTMapElem4011,
    4030:QQTMapElem4030,
    4031:QQTMapElem4031,
    4032:QQTMapElem4032,
    4034:QQTMapElem4034,
    4035:QQTMapElem4035,
    4036:QQTMapElem4036,
    4037:QQTMapElem4037,
    4038:QQTMapElem4038,
    2013:QQTMapElem2013,
    2017:QQTMapElem2017,
    2018:QQTMapElem2018,
    2020:QQTMapElem2020,
    2025:QQTMapElem2025,
    2026:QQTMapElem2026,
    2028:QQTMapElem2028,
    2029:QQTMapElem2029,
    2037:QQTMapElem2037,
    2038:QQTMapElem2038,
    2042:QQTMapElem2042,
    2043:QQTMapElem2043,
    2044:QQTMapElem2044,
    2046:QQTMapElem2046,
    2047:QQTMapElem2047,
    17026:QQTMapElem17026,
    17029:QQTMapElem17029,
}
