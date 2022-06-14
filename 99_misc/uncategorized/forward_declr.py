
# Global Imports
import os
import scipy.io
import numpy as np


# Local Imports
from nnf.core.iters.custom.WindowIter import *
from nnf.db.NNdb import NNdb

from nnf.db.Selection import Selection

# def foo():
#     bar()
#
# def bar():
#     print("bar")
#
#
# # Functions must be declared before its usage, but not its declaration.
# foo()

class PublicClass:
    def __init__(self):
        pass


class Forward:
    @staticmethod
    def foo():
        fn = Forward._bar
        Forward._invoke(fn)

    @staticmethod
    def _bar():
        print("bar")

    @staticmethod
    def _invoke(fn):
        fn()

Forward.foo()


# Ref: https://stackoverflow.com/questions/41921255/staticmethod-object-is-not-callable-switch-case
# You are storing unbound staticmethod objects in a dictionary. Such objects (as well as classmethod objects,
# functions and property objects) are only bound through the descriptor protocol, by accessing the name as an
# attribute on the class or an instance
class A(object):
    @staticmethod
    def open():
        return 555

    @staticmethod
    def proccess():
        return 456

    # i = 10
    # value = A.i  # Error: name 'A' is not defined
    call_open = open

    switch = {
        1: open,
        2: proccess,
        }
# obj = A.switch[1]()
A.call_open()




# Get the current working directory, define a `DataFolder`
data_folder = r'F:\#DL_THEANO\Workspace\DL\DLN\DataFolder'

# Load image database `AR`
matStruct = scipy.io.loadmat(os.path.join(data_folder, 'IMDB_66_66_AR_8.mat'),
                             struct_as_record=False, squeeze_me=True)
imdb_obj = matStruct['imdb_obj']
nndb = NNdb('original', imdb_obj.db, 8, True)
# nndb = nndb.zero_to_one

# Training, Validation, Testing Split Definition
sel = Selection()
# sel.use_rgb = False
# sel.histeq = True
# sel.scale = [33, 33] #(128, 128) #(150, 150)  #(100, 100) #(224, 224)
sel.tr_col_indices = np.uint16(np.arange(0, 7))
sel.val_col_indices = np.uint16(np.arange(7, 8))
# sel.te_col_indices = np.uint16(np.array([7]))
sel.class_range = np.uint8(np.arange(0, 100))


db_dir = os.path.join(data_folder, "disk_db")
window_iter = WindowIter([2, 4, 5], [1, 2, 2])
wnd_counts, duration  = Window.get_total_wnd_counts(nndb, sel, window_iter)

import pickle
def save(destination_dir, obj):
    """Save this nndiskman to disk.

    Parameters
    ----------
    destination_dir : str
        Path to the folder that contains the `diskman.pkl` file.
    """
    pkl_fpath = destination_dir  #os.path.join(destination_dir, 'diskman.pkl')

    # IMPORTANT: This will serialize this object including `sel` object with sel.nnpatches.
    # If extended `NNPatch` object contains a non-serializable attribute, this method will fail.
    try:
        # Pickle the self object using the highest protocol available.
        with open(pkl_fpath, "wb") as f:
            pickle.dump(obj, f, -1)

    except Exception as e:
        # Unpickling failed
        print("Pickle failed. Possibly due to a non-serializable attribute in extended `NNPath` object.")
        raise pickle.UnpicklingError(repr(e))


save(r'D:\diskman.pkl', window_iter)