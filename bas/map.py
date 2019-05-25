import tmx


class Map:
    def __init__(self, file_path):
        self.file_path = file_path
        self.height = None
        self.width = None
        self.__map = None
        self.__tilesets = None

    @property
    def map(self):
        return self.__map

    def load(self):
        tmx_map = tmx.TileMap.load(self.file_path)
        self.height = tmx_map.height
        self.width = tmx_map.width
        self.__load_map_info(tmx_map)

    def __load_map_info(self, tmx_map):
        if tmx_map.renderorder != 'right-down':
            raise Exception('Error loading map: Wrong render order')
        w = self.width
        h = self.height
        self.__map = [[{} for x in range(w)] for y in range(h)]
        self.__tilesets = tmx_map.tilesets
        for layer in tmx_map.layers:
            self.__load_layer_info(layer)
        return

    def __load_layer_info(self, layer):
        for i in range(self.height):
            for j in range(self.width):
                layer_tile = layer.tiles.pop(0)
                if layer_tile.gid != 0:
                    self.__map[i][j][layer.name] = self.__get_tile_info(layer_tile)
        return

    def __get_tile_info(self, tile):
        tile_info = {'tile-id': tile.gid}
        tileset_tile = self.__get_tileset_tile(tile.gid)
        if tileset_tile is not None:
            tile_info['properties'] = self.__get_tile_properties(tileset_tile)
        return tile_info

    def __get_tileset_tile(self, tile_gid):
        for tileset in self.__tilesets:
            for tile in tileset.tiles:
                if tile_gid == tile.id + 1:
                    return tile
        return None

    def __get_tile_properties(self, tile):
        tile_properties = {}
        for _property in tile.properties:
            tile_properties[_property.name] = _property.value
        return tile_properties

