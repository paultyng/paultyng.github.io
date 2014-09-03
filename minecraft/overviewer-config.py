resources = [Base(), EdgeLines(), MineralOverlay(), SlimeOverlay(), SmoothLighting()]

worlds['My World'] = "C:\\users\\Paul\\AppData\\Roaming\\.minecraft\\saves\\server-201409011826"

outputdir = "D:\\github\\paultyng.github.io\\minecraft"

texturepath = "C:\\Users\\Paul\\AppData\\Roaming\\.minecraft\\versions\\1.8\\1.8.jar"

rendermode = "smooth_lighting"

renders["render1"] = {
        'world': 'My World',
        'northdirection': 'upper-left',
        'title': 'SW',
}

renders["render2"] = {
        'world': 'My World',
        'northdirection': 'upper-right',
        'title': 'SE',
}

renders["render3"] = {
        'world': 'My World',
        'northdirection': 'lower-right',
        'title': 'NE',
}

renders["render4"] = {
        'world': 'My World',
        'northdirection': 'lower-left',
        'title': 'NW',
}

renders["render5"] = {
        'world': 'My World',
        'title': 'Nighttime',
        'rendermode': 'smooth_night',
}

renders["render6"] = {
        'world': 'My World',
        'title': 'Cave',
        'rendermode': 'cave',
}

renders["render7"] = {
        'world': 'My World',
        'title': 'Nether',
        'dimension': 'nether',
        'rendermode': 'nether_smooth_lighting',
}

renders["render8"] = {
        'world': 'My World',
        'title': 'Resources',
        'rendermode': resources,
}


