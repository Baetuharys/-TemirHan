"""First-pass forced-air heat balance. Not a substitute for component derating/thermal simulation."""
def required_airflow_m3h(heat_w:float, delta_t_k:float, air_density_kg_m3:float=1.2, cp_j_kgk:float=1005.0)->float:
    if heat_w < 0: raise ValueError('heat_w must be >=0')
    if delta_t_k <= 0 or air_density_kg_m3 <= 0 or cp_j_kgk <= 0: raise ValueError('delta_t, density, cp must be >0')
    m3_s=heat_w/(air_density_kg_m3*cp_j_kgk*delta_t_k)
    return m3_s*3600
