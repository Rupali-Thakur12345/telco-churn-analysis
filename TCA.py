import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=r"C:\Users\user\Downloads\datset of project\archive (1)\WA_Fn-UseC_-Telco-Customer-Churn.csv"
df = pd.read_csv(df)
print(df)
print(df.info())
print(df.columns)
#replace the blank with 0 as tenure is 0 and no total charge are recorded
replace_blank=df['TotalCharges']=df['TotalCharges'].replace(" ","0")
change_dtype=df['TotalCharges']=df['TotalCharges'].astype("float")
print(replace_blank)
print(change_dtype)
print(df.info())

print(df.isna().sum())
print(df.describe())
print(df.duplicated().sum)
#check duplicates based on customer id
print(df["customerID"].duplicated().sum)
# convert 0 and 1 values of senoir citizen to yes/no to make it easier to understand
def convert(value):
   if value ==1:
    return "yes"
   else :
     return "no"
change=df["SeniorCitizen"]=df["SeniorCitizen"].apply(convert)
print(change)
print(df.head)

ax=sns.countplot(x='Churn',data= df)
ax.bar_label(ax.containers[0])
plt.show()
# gb= df.groupby("Churn").agg(['Churn'"count"])
# plt.pie(gb['Churn'],labels= gb.index,autopct="%1.2f%%")
# plt.show()

print(df.columns)
plt.figure(figsize=(3,4))
sns.countplot(x=df["gender"],data=df,hue="Churn")
plt.title("Churn by gender")
plt.show()

plt.figure(figsize=(3,4))
sns.countplot(x=df["SeniorCitizen"],data=df,hue="Churn")
plt.title("churn by seniorcitizen")
plt.show()

plt.figure(figsize=(5,5))
sns.histplot(x="tenure",data=df,bins=72,hue="Churn")
plt.title("tenure of the customer")
plt.show()
#people who are used our services for along time have stayed and people who have used our services
#for 1 or 2 month have churned

print(df.columns)
plt.figure(figsize=(3,4))
ab=sns.countplot(x=df["Contract"],data=df,hue="Churn")
ab.bar_label(ab.containers[0])
plt.title("count of customer by contract")
plt.show()
# People who have month to month contract are likely churn than from whose 1 or 2 years of contract

#list of columns for which we wnat to craete count plot
columns=['PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup',
         'DeviceProtection','TechSupport','StreamingTV','StreamingMovies']

#number of column for the subject grid (you can change this)
n_cols=3
n_rows=(len(columns)+n_cols-1)//n_cols #calculate number of rows needed

#create subplot
fig,axes=plt.subplots(n_rows,n_cols,figsize=(15,n_rows*4)) # adjust figsize as neede

axes=axes.flatten()

# Iterate over columns and plot count plots
for i, col in enumerate(columns):
  sns.countplot(x=col, data=df,ax=axes[i],hue='Churn')
  axes[i].set_title(f'Count plot os (col)')
  axes[i].set_xlabel(col)
  axes[i].set_ylabel('Count')

# Remove empty subplot (if any)
for j in range (i+1,len(axes)):
  fig.delaxes(axes[j])
plt.tight_layout()
plt.show()   

#People who are using fiber optice arelikely to churn,people who are using multiplines are also churing in good amount 
#and in phone services is descent
# People who are not using online security are churing

plt.figure(figsize=(7,7))
ab=sns.countplot(x=df["PaymentMethod"],data=df,hue="Churn")
ab.bar_label(ab.containers[0])
ab.bar_label(ab.containers[1])
plt.xticks(rotation=45)
plt.title("Churned Customer by Payment Method ")
plt.show()
