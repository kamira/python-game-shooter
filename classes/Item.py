# 設定物件大小
class ObjectSize(object):
    def __init__(self):
        pass
    def setSize(self, size):
        w, h = size
        self.__width = w
        self.__height = h
    def getSize(self):
        return self.__width, self.__height

# 設定物件是否為玩家及圖案
class ObjectPlayer(object):
    def __init__(self):
        pass
    def setPlayerStatus(self, player = False):
        self.__player = player
    def getPlayerStatus(self):
        return self.__player
    def setPlayerSprite(self, spr = None):
        self.__sprite = spr
    def getPlayerSprite(self):
        return self.__sprite

# 設定玩家可移動範圍
class PlayerArea(object):
    def __init__(self):
        pass
    def setPlayerArea(self, area):
        xs, xe, ys, ye = area
        self.__player_X_Start = xs
        self.__player_X_End = xe
        self.__player_Y_Start = ys
        self.__player_Y_End = ye
    def getPlayerArea(self):
        return [self.__player_X_Start, self.__player_X_End, self.__player_Y_Start, self.__player_Y_End]


# 設定物件座標系統
class ObjectCoordinate(ObjectSize, ObjectPlayer, PlayerArea):
    # 物件座標系統 Class 初始化
    def __init__(self):
        # 不設定任何參數，直接略過
        pass
    # 設定物件座標
    def setCoordination(self, coor):
        (x,y) = coor
        self.__x = x
        self.__y = y
    # 移動物件座標
    def movCoordination(self, coor):
        (x,y) = coor
        w,h = super().getSize()
        # 確認是否為玩家本身
        if super().getPlayerStatus() :
            # print("X: " + str(x) + ";Y: " + str(y) )
            newX = self.__x + x
            newY = self.__y + y
            # print("New X: " + str(newX) + ";New Y: " + str(newY) )
            (areaWS, areaWE, areaHS, areaHE) = super().getPlayerArea()
            # print(str(areaWS) + ";" + str(areaWS) + ";" + str(areaHS) + ";" + str(areaHE) )
            # 避免超過玩家移動區域
            if ( newX > areaWS ) and ( ( newX + w ) < areaWE ):
                self.__x = newX
            elif newX <= areaWS:
                self.__x = areaWS
            
            if ( newY > areaHS ) and ( ( newY + h ) < areaHE ):
                self.__y = newY
            elif newY <= areaHS:
                self.__y = areaHS

        # 若非玩家則依照原本設定的位移量位移
        else:
            self.__x = self.__x + self.__speedInX
            self.__y = self.__y + self.__speedInY
    # 獲得物件的XY座標
    def getCoordination(self):
        return self.__x, self.__y
    # 設定物件在XY坐標系上的速度
    def setSpeed(self, coor):
        (x,y) = coor
        self.__speedInX = x
        self.__speedInY = y
    def getSpeed(self):
        return self.__speedInX, self.__speedInY

class Item(ObjectCoordinate):
    def __init__(self, objectCoordinationArray = [0,0], objectSizeArray = [0,0], objectSpeed = [0,0], spr = None, player = False, moveAreaArray = [0,0,0,0], time_to_die = 999):
        # objectCoordination 為物件座標
        super().setCoordination(objectCoordinationArray)
        # objectWidth, objectHeight 分別為物件的寬與高
        super().setSize(objectSizeArray)
        # moveArea 依序為X座標開始, X座標結束, Y座標開始, Y座標結束的矩形區域
        super().setPlayerArea(moveAreaArray)
        # player 為設定該物件是否為玩家
        super().setPlayerStatus(player)
        # objectSpeed 為物件在XY的每次位移量
        super().setSpeed(objectSpeed)
        #
        super().setPlayerSprite(spr)
        self._ttl = time_to_die
    def getObjectXYByList(self):
        return super().getCoordination()
    def getObjectXYByTuple(self):
        x,y = super().getCoordination()
        return (x, y)
    def getObjectX(self):
        x,y = super().getCoordination()
        return x
    def getObjectY(self):
        x,y = super().getCoordination()
        return y
    def getObjectSize(self):
        return super().getSize()
    def getObjectWidth(self):
        w,h = super().getSize()
        return w
    def getObjectHeight(self):
        w,h = super().getSize()
        return h
    def getObjectSprite(self):
        return super().getPlayerSprite()
    def setObjectSpeed(self, coor):
        super().setSpeed(coor)
    def getObjectSpeed(self):
        return super().getSpeed()
    def movObjectCoordination(self, coor = [0,0]):
        super().movCoordination(coor)
    def setTTL(self, time_to_die):
        self._ttl = time_to_die
    def getTTL(self):
        return self._ttl
    def doTTL(self):
        self._ttl -= 1