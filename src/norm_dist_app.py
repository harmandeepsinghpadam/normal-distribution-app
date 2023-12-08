from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def create_pdf(mean=30,std=5,alpha=0.3,color='blue',std_color='black'):

    age_distribution=stats.norm(loc=mean,scale=std)
    sample=age_distribution.rvs(1000)

    data = np.linspace(min(sample), max(sample), num=1000)
    pdf_vals=age_distribution.pdf(x=data)

    plt.ylabel("Probability Density")
    plt.xlabel("Age")

    plt.plot(data,pdf_vals,alpha=alpha,color=color)

    std_o=age_distribution.pdf(x=mean)
    plt.plot([mean,mean],[0,std_o],alpha=alpha,linestyle='dashed',color=std_color)

    std_1=age_distribution.pdf(x=mean+std)
    plt.plot([mean+std,mean+std],[0,std_1],alpha=alpha,linestyle='dashed',color=std_color)

    std_2=age_distribution.pdf(x=mean+2*std)
    plt.plot([mean+2*std,mean+2*std],[0,std_2],alpha=alpha,linestyle='dashed',color=std_color)

    std_min1=age_distribution.pdf(x=mean-std)
    plt.plot([mean-std,mean-std],[0,std_min1],alpha=alpha,linestyle='dashed',color=std_color)

    std_min2=age_distribution.pdf(x=mean-2*std)
    plt.plot([mean-2*std,mean-2*std],[0,std_min2],alpha=alpha,linestyle='dashed',color=std_color)

    plt.annotate(str(std_min2.round(3)),xy=(mean-2*std-2,std_min2),alpha=alpha)
    plt.annotate(str(std_min1.round(3)),xy=(mean-1*std-2,std_min1),alpha=alpha)
    plt.annotate(str(std_o.round(3)),xy=(mean-2,std_o),alpha=alpha)
    plt.annotate(str(std_1.round(3)),xy=(mean+std-2,std_1),alpha=alpha)
    plt.annotate(str(std_2.round(3)),xy=(mean+2*std-2,std_2),alpha=alpha)
    plt.title('PDF')

def create_cdf(mean=30,std=5,alpha=0.3,color='blue',std_color='black'):

    age_distribution=stats.norm(loc=mean,scale=std)
    sample=age_distribution.rvs(1000)

    data = np.linspace(min(sample), max(sample), num=1000)
    cdf_vals=age_distribution.cdf(x=data)


    plt.plot(data,cdf_vals,alpha=alpha,color=color)
    plt.ylabel("Probability")
    plt.xlabel("Age")

    std_o=age_distribution.cdf(x=mean)
    plt.plot([mean,mean],[0,std_o],alpha=alpha,linestyle='dashed',color=std_color)

    std_1=age_distribution.cdf(x=mean+std)
    plt.plot([mean+std,mean+std],[0,std_1],alpha=alpha,linestyle='dashed',color=std_color)

    std_2=age_distribution.cdf(x=mean+2*std)
    plt.plot([mean+2*std,mean+2*std],[0,std_2],alpha=alpha,linestyle='dashed',color=std_color)

    std_min1=age_distribution.cdf(x=mean-std)
    plt.plot([mean-std,mean-std],[0,std_min1],alpha=alpha,linestyle='dashed',color=std_color)

    std_min2=age_distribution.cdf(x=mean-2*std)
    plt.plot([mean-2*std,mean-2*std],[0,std_min2],alpha=alpha,linestyle='dashed',color=std_color)

    plt.annotate(str(std_min2.round(3)),xy=(mean-2*std-2,std_min2),alpha=alpha)
    plt.annotate(str(std_min1.round(3)),xy=(mean-1*std-2,std_min1),alpha=alpha)
    plt.annotate(str(std_o.round(3)),xy=(mean-2,std_o),alpha=alpha)
    plt.annotate(str(std_1.round(3)),xy=(mean+std-2,std_1),alpha=alpha)
    plt.annotate(str(std_2.round(3)),xy=(mean+2*std-2,std_2),alpha=alpha)

    plt.title('CDF')


    # st.image("src/icons/nom_distr_icon.png")


st.title("Normal distribution")
# st.write("In statistics, a normal distribution or Gaussian distribution is a type of continuous probability distribution for a real-valued random variable.")
st.write("Normal distributions are important in statistics and are often used in the natural and social sciences to represent real-valued random variables whose distributions are not known. Their importance is partly due to the central limit theorem. It states that, under some conditions, the average of many samples (observations) of a random variable with finite mean and variance is itself a random variable—whose distribution converges to a normal distribution as the number of samples increases. Therefore, physical quantities that are expected to be the sum of many independent processes, such as measurement errors, often have distributions that are nearly normal.")
latext = r'''
$$
\text {Notation}={\mathcal {N}}(\mu ,\sigma ^{2})
$$
$$
\text {Mean}=\mu
$$
$$
\text {Standard Deviation}=\sigma
$$
$$
\text {Probability density function}, PDF= {\displaystyle {\frac {1}{\sigma {\sqrt {2\pi }}}}e^{-{\frac {1}{2}}\left({\frac {x-\mu }{\sigma }}\right)^{2}}}
$$
$$
\text {Cumulative distribution function}, CDF={\displaystyle {\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{x}e^{-t^{2}/2}\,dt}
$$

'''
st.write(latext)

st.header("Observe the impact of mean and standard deviation on the PDF and CDF of a Normal or Gaussian Distribution ")

# st.sidebar.image('src/icons/614251-200.png')
st.sidebar.image('src/icons/1827272.png')
st.sidebar.header("Normal Distribution")
st.sidebar.text('''In statistics, a 
normal distribution or 
Gaussian distribution 
is a type of 
continuous probability 
distribution for a 
real-valued random 
variable.''')


    # st.write("Normal Distribution")
    

#Input mean and std
mean = st.slider('Select mean Age', 0, 50, 30)
st.write("Mean Age=",mean)

std = st.slider('Select standard deviation', 0, 50, 5)
st.write("Standard deviation =",std)

#Plot PDF
fig=plt.figure(figsize=(5,4))
plt.grid()
create_pdf()
create_pdf(mean=mean,std=std,color='red',alpha=1)
st.pyplot(fig)

#Plot CDF
fig=plt.figure(figsize=(5,4))
plt.grid()
create_cdf()
create_cdf(mean=mean,std=std,color='red',alpha=1)
st.pyplot(fig)
