from typing import Self
from enum import Enum
from collections import defaultdict
from typing import TypedDict

class ProcessType(Enum):
    PVD = 'Physical_Vapor_Deposition'
    CVD = 'Chemical_Vapor_Deposition'
    ALD = 'Atomic_Layer_Deposition'
    LITHO = 'Litho'
    DRY_ETCH = 'Dry_Etch'
    WET_ETCH = 'Wet_Etch'

MODULE_MAP: dict[str, set[ProcessType]] = {
    'Thin_Film': {ProcessType.PVD, ProcessType.CVD, ProcessType.ALD},
    'Lithography': {ProcessType.LITHO},
    'Etching': {ProcessType.DRY_ETCH, ProcessType.WET_ETCH}
}

class Machine:
    total_machines: dict[str, int] = defaultdict(int)
    total_available_time: dict[str, int] = defaultdict(int)

    def __init__(self, process_type: ProcessType, available_time: int) -> None:
        self.process_type = process_type
        self.available_time = available_time
        self._update_state()
    
    def _update_state(self) -> bool:
        for module, types in MODULE_MAP.items():
            if self.process_type in types:
                Machine.total_machines[module] += 1
                Machine.total_available_time[module] += self.available_time
                return True
        return False

    @classmethod
    def auto_capacity(cls, process_type: ProcessType) -> Self:
        database: dict[ProcessType, int] = {
            ProcessType.PVD: 1_500,
            ProcessType.CVD: 1_000,
            ProcessType.ALD: 1_300,
            ProcessType.LITHO: 1_000,
            ProcessType.DRY_ETCH: 2_000,
            ProcessType.WET_ETCH: 1_800
        }
        capacity: int | None = database.get(process_type)
        
        if capacity:
            print(f"Setting capacity to: {capacity}")
        else:
            print(f'Could not find: "{process_type}" in our database. Using default fo 1_000.')
            capacity = 1_000
        
        return cls(process_type=process_type, available_time=capacity)
    
    @classmethod
    def total_machines_created(cls) -> dict:
        return cls.total_machines
    
    @classmethod
    def total_machines_available_time(cls) -> dict:
        return cls.total_available_time
    
    def __str__(self) -> str:
        return f'{self.process_type.name} Machine (Cap: {self.available_time} min)'

class Product(TypedDict):
    name: str
    std_proc_time: int # 每一片 (pc) 或每一批 (lot) 需要的標準工時

class Lot:
    def __init__(self, lot_id: str, qty: int, product: Product):
        self.lot_id = lot_id
        self.qty = qty
        self.product = product
    
    
    def get_required_capacity(self) -> int:
        """
        計算此 Lot 需要消耗多少產能 (時間)
        公式：數量 * 標準工時
        """
        return self.qty * self.product['std_proc_time'] 

def main():
    m1: Machine = Machine.auto_capacity(ProcessType.ALD)
    print(m1)

    m2: Machine = Machine.auto_capacity(ProcessType.CVD)
    print(m2)

    m3: Machine = Machine.auto_capacity(ProcessType.LITHO)
    print(m3)

    m4: Machine = Machine.auto_capacity(ProcessType.LITHO)
    print(m4)

    m5: Machine = Machine.auto_capacity(ProcessType.DRY_ETCH)
    print(m5)

    m6: Machine = Machine.auto_capacity(ProcessType.WET_ETCH)
    print(m6)
    print(Machine.total_machines_created())
    print(Machine.total_machines_available_time())

    p1: Product = {'name': 'Chip_A', 'std_proc_time': 15} # 15 min / pc
    my_lot = Lot(lot_id="L001", qty=10, product=p1)

    print(f"Lot {my_lot.lot_id} 需要產能: {my_lot.get_required_capacity()} 分鐘")

if __name__ == "__main__":
    main()
