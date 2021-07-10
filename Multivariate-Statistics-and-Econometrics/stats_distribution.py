#!/usr/bin/env python
# coding: utf-8

# ### Normality test

# In[95]:


from scipy.stats import normaltest

def check_normality(data):

    z_stat, p_val = normaltest(data)

    print('z_stat=%.3f, p_val=%.3f' % (z_stat, p_val))

    if p_val > 0.05:
        print('Probably Normal')
    else:
        print('Probably not Normal')


# ## Z distribution

# In[78]:


from scipy.stats import norm, t, chi2, f


# In[18]:


# standard normal distrbn. area to the left 
norm.cdf(-0.77)


# In[19]:


# to get z area to right use -1 * z
norm.cdf(-1 * -0.77)


# In[43]:


# function to get pvalue given z score and position
def z_to_pval(zscore, pos="left"):
    
    if pos == "right":
        return norm.cdf(-1 * zscore)
    elif pos == "left": 
        return norm.cdf(zscore)  
    else:
        print("invalid position")
  
    
    


# In[44]:


z_to_pval(-1.5, "left")


# In[29]:


# get zscore from pvalue, for area to the left

norm.ppf(0.0668)


# In[32]:


# get zscore from pvalue, -1* for area to the right
-1 * norm.ppf(0.94)


# In[41]:


# function to get zscore given p value and position
def pval_to_z(pval, pos="left"):
    
    if pos == "right":
        return -1 * norm.ppf(pval)
    elif pos == "left": 
        return norm.ppf(pval)
    else:
        print("invalid position")
  


# In[42]:


pval_to_z(0.94, "right")


# ### T distribution

# In[51]:


# get p value to left from t score
# to get t area to right use -1 * t

t.cdf(1.2, df = 2)


# In[55]:


# function to get pvalue given t score and position
def t_to_pval(tscore, df, pos="left"):
    
    if pos == "right":
        return t.cdf(-1 * tscore, df)
    elif pos == "left": 
        return t.cdf(tscore, df)  
    else:
        print("invalid position")
  
    
    


# In[56]:


t_to_pval(1.2, 2, "right")


# In[49]:


# get t score from p value to left
t.ppf(0.8234, df = 2)


# In[57]:


# function to get zscore given p value and position
def pval_to_t(pval, df, pos="left"):
    
    if pos == "right":
        return -1 * t.ppf(pval, df)
    elif pos == "left": 
        return t.ppf(pval, df)
    else:
        print("invalid position")
  


# In[59]:


pval_to_t(0.8234, 2, "right")


# ## chi square distribution

# In[61]:


# get p value to left for chi square stat
chi2.cdf(3.84, df = 1 )


# In[63]:


# for right area
1 - chi2.cdf(3.84, df = 1 )


# In[65]:


# function to get pvalue given chi2 score and position
def chi2_to_pval(chi2score, df, pos="left"):
    
    if pos == "right":
        return 1 - chi2.cdf(chi2score, df)
    elif pos == "left": 
        return chi2.cdf(chi2score, df)  
    else:
        print("invalid position")
  
    
    


# In[77]:


chi2_to_pval(0.3172, 2, "right")


# In[73]:


# get chi stat for pvalue to left
chi2.ppf(0.8533, 2)


# In[68]:


# function to get chi2 score given p value and position
def pval_to_chi2(pval, df, pos="left"):
    
    if pos == "right":
        return chi2.ppf(1 - pval, df)
    elif pos == "left": 
        return chi2.ppf(pval, df)
    else:
        print("invalid position")
  


# In[76]:


pval_to_chi2(0.8533, 2, "right")


# ## F distribution

# In[83]:


f.cdf(1.5, 2, 3)


# In[85]:


# function to get pvalue given f score and position
def f_to_pval(fscore, df1, df2, pos="left"):
    
    if pos == "right":
        return 1 - f.cdf(fscore, df1, df2)
    elif pos == "left": 
        return f.cdf(fscore, df1, df2)  
    else:
        print("invalid position")
  
    


# In[90]:


f_to_pval(1.5, 2, 3, "left")


# In[84]:


f.ppf(0.64645, 2, 3)


# In[88]:


# function to get f score given p value and position
def pval_to_f(pval, df1, df2, pos="left"):
    
    if pos == "right":
        return f.ppf(1 - pval, df1, df2)
    elif pos == "left": 
        return f.ppf(pval, df1, df2)
    else:
        print("invalid position")
  


# In[92]:


pval_to_f(0.64644, 2, 3,"left")


# In[ ]:




