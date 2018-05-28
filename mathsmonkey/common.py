from mathsmonkey import settings

class pdf_gen:
    """
    base class for all pdf generating classes
    """
    def out_dir(self):
        return settings.pdf_out_root

    def pge_geom(self):
        return {"tmargin" : "1cm",  "bmargin" : "1cm",  "lmargin" : "1cm",  "rmargin" : "1cm" }
