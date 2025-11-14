import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('nilai_siswa.csv')
data.info()
data.head()
data.describe()
print("rata-rata:", data['Nilai'].mean())
print("median:", data['Nilai'].median())
print("mnodus:", data['Nilai'].mode()[0])


print('--------------------------------------------')

matematika = data[data['Matpel'] == 'Matematika']
print("rata-rata Matematika:", matematika['Nilai'].mean())
print("median Matematika:", matematika['Nilai'].median())
print("modus Matematika:", matematika['Nilai'].mode()[0])
print(matematika)


print('--------------------------------------------')


bahasa_indonesia = data[data['Matpel'] == 'Bahasa Indonesia']
print("rata-rata Bahasa Indonesia:", bahasa_indonesia['Nilai'].mean())
print("median Bahasa Indonesia:", bahasa_indonesia['Nilai'].median())
print("modus Bahasa Indonesia:", bahasa_indonesia['Nilai'].mode()[0])
print(bahasa_indonesia)


print('--------------------------------------------')


fisika = data[data['Matpel'] == 'Fisika']
print("rata-rata Fisika:", fisika['Nilai'].mean())
print("median Fisika:", fisika['Nilai'].median())
print("modus Fisika:", fisika['Nilai'].mode()[0])
print(fisika)


print('--------------------------------------------')


bahasa_inggris = data[data['Matpel'] == 'Bahasa Inggris']
print("rata-rata Bahasa Inggris:", bahasa_inggris['Nilai'].mean())
print("median Bahasa Inggris:", bahasa_inggris['Nilai'].median())
print("modus Bahasa Inggris:", bahasa_inggris['Nilai'].mode()[0])
print(bahasa_inggris)


print('--------------------------------------------')


produktif = data[data['Matpel'] == 'Produktif']
print("rata-rata Produktif:", produktif['Nilai'].mean())
print("median Produktif:", produktif['Nilai'].median())
print("modus Produktif:", produktif['Nilai'].mode()[0])
print(produktif)


print('--------------------------------------------')


data.groupby('Matpel')['Nilai'].agg(['max','min'])
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('rata-rata Nilai per Matpel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai rata-rata')
plt.tight_layout()
plt.show()


print('--------------------------------------------')


sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Distribusi Nilai per Matpel')
plt.tight_layout()
plt.show()
print('--------------------------------------------')
