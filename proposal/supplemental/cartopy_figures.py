# GH Issue 363
# https://github.com/SciTools/cartopy/issues/363#issuecomment-770311997

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt


central_lon, central_lat = 180, 30
ax = plt.axes((0, 0, 1, 1), projection=ccrs.Orthographic(central_lon, central_lat))
ax.set_extent([-106, 135, 28, 45], crs=ccrs.Geodetic())

geodetic = ccrs.Geodetic()

# Japan info
lat_jap, lon_jap = 36.204823, 138.252930
# California info
lat_cal, lon_cal = 36.778259, -119.417931

# California -> Japan
ax.plot([-119.417931, 138.252930],[36.778259, 36.204823], color='b', transform=geodetic)
# Reverse: Japan -> California
ax.plot([-119.417931, 138.252930][::-1],[36.778259, 36.204823][::-1], color='r', transform=geodetic)

ax.plot(lon_jap, lat_jap, markersize=10, marker='o', color='k', transform=geodetic)
ax.plot(lon_cal, lat_cal, markersize=10, marker='o', color='k', transform=geodetic)

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

# Add another line with a finer threshold to demonstrate what we want it to be
ortho2 = ccrs.Orthographic(central_lon, central_lat)
ortho2._threshold = 1000
ax2 = plt.axes((0, 0, 1, 1), projection=ortho2)
ax2.set_extent([-106, 135, 28, 45], crs=ccrs.Geodetic())
ax2.patch.set_visible(False)
ax2.plot([-119.417931, 138.252930],[36.778259, 36.204823], color='k', linestyle="--", linewidth=1, transform=geodetic)

plt.savefig("cartopy_interpolation.png", bbox_inches='tight')
# plt.show()
