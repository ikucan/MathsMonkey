from mathsmonkey import settings

class pdf_gen:
    """
    base class for all pdf generating classes
    """
    def out_dir(self):
        return settings.pdf_out_root
