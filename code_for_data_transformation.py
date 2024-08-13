import pandas as pd

df = pd.read_csv(r'food_claims_2212_python.csv', 
                 dtype = 
                 {'claim_id': int,'claim_amount': str, 'time_to_close':int,'amount_paid': str,
		'location': str,
		 'individuals_on_claim': int, 
                 'linked_cases': str,
                 'cause': str})

#to remove some wierd currency symbol
df['claim_amount'] = df.claim_amount.str.slice(3,)


#working on the missing values of amount_paid column:
median_amount_paid = round(df.amount_paid.median(),2)
df['amount_paid'] = df.amount_paid.replace(to_replace = np.nan,
 value = median_amount_paid)



#replace the missing values of 'linked_cases' with False:
df['linked_cases'] = df.linked_cases.replace(np.nan, False)


#fixing the value inconsistency:
df['cause'] = df.cause.replace(to_replace = ['VEGETABLES', ' Meat'],
 value = ['vegetable', 'meat'])


#convert both claim_amount & amount_paid to float type
df['claim_amount'] = df.claim_amount.astype(float)

df['amount_paid'] = df.amount_paid.astype(float)


#convert 'location' values from all caps to title case
df['location'] = df['location'].str.title()






