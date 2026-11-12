import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


def test_openfc_imports_resolve_from_src_layout():
    import openfc
    from openfc.componentMap import ComponentMap
    from openfc.components.breedingBlanket import BreedingBlanket
    from openfc.components.component import Component
    from openfc.components.fuelingSystem import FuelingSystem
    from openfc.components.plasma import Plasma
    from openfc.port import Port
    from openfc.simulate import Simulate
    from openfc.tools.utils import visualize_connections

    assert openfc is not None
    assert Component is not None
    assert FuelingSystem is not None
    assert Plasma is not None
    assert BreedingBlanket is not None
    assert ComponentMap is not None
    assert Port is not None
    assert Simulate is not None
    assert visualize_connections is not None
