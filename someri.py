import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
data_pre_covid = pd.read_csv("../educatie.csv")
data_post_covid = pd.read_csv("../nivel-educatie.csv")

print(data_pre_covid)
print(data_post_covid)

sns.barplot(x=data_post_covid['JUDET  '], y=data_post_covid['Total someri, din care: '], label="Numar someri mai 2020", color="blue")
plt.xticks(
    rotation=45,
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-small'
)

sns.barplot(x=data_pre_covid['JUDET  '], y=data_pre_covid['Total someri, din care: '], label="Numar someri inainte de pandemie", color="orange")
plt.xticks(
    rotation=45,
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-small'
)
#plt.show()


#plt.show()

plt.ylabel("Numar someri")
#plt.show()
plt.legend()
plt.title("Numar total de someri inainte si dupa ridicarea restrictiilor")
plt.savefig("someri.png", bbox_inches='tight', dpi = 300)