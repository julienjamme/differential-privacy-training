# ESTP Training on DP

## Confidentiality at risk : re-identification and value disclosure attacks

Indonesia / Germany / BCE / Albania / Turquie / Korea (Bank of Korea) / Ireland / Slovakia / Italia 


### Privacy definition 

confidentiality is one aspect of privacy
no formal definition of privacy
one in universal declaration of human rights
IT or lawyers or statisticians 

relationship to privacy is different for one domain to another
ex: use medical records to search new drugs
use mobility data for disater response
tax data for fighting against fiscal evasion 

=> depends on social acceptance !

### Links between laws and  techno

very old law in the US from 1890 => because of apparition of photography 
law still used but new technologies and the links between both laws and tech are evolving continuously


### Statistical confidentiality

NSI good practice: UN need to ensure confidentiality 

- keeping data secret or private (very simple concept: is it secret or not ?) = focus of the training
=> security : preventing unauthorized access
=> SDC : techniques to ensure that no entity is identifiable from released data

### Disclosure vs Inference

- Disclosure: identitification within the data collected and released
- Statistical Inference : probability that we infer sensitive data from released data 
risk of inference has to be done manually (is it ok or not to let inference on some knowledge)

### Main attacks : linkage reconstruction, membership

(is reconstruction really an attack ?)

#### Linkage attacks

release of microdata
use of an auxiliary source to deanonymize a dataset (Sweeney) 
non identifier data becoing identifying.

Example of Netflix: based on the linkage between netflix and IMDB

Identification is not determined by the nature of the data but by the sheer quantity: the more data, the more unique.

what is problematic is how much you disclose not really what you disclose.
personal tastes, use frequencies etc. => we are unique 

Available auxiliary information cannot be anticipated ! 

Conventional techniques: pseudonymization, hashing, or remove persoanl identifiers, aggregation, k-anonymity, generalization

#### Reconstruction attacks

realease of aggregated statistics => reconstruction of microdata is possible

success on the number of statistics released
solution of a system of equation.
example from Census Bureau

reconstruction is possible even when fewer statistics than rows 
missing data can be reconstructed with auxiliary information.

reconstruction does not need to be exact to cause harm

#### Membership attacks

Was an individual in the data collected from which the aggregated data were produced.
The success of this attack is guaranteed if the exact statistcis is released or the models.

THe sensitive attribute 
Infer the sensitive attribute for the other one (if we know it for the)

transition douce vers la DP (statistique avec Alice vs statistique sans ALice)

Very strong assumption: we know all bt Alice

But some data (sensitive) are already available for some attacker:
HIV status => insurance
Financial Status => Bank
HH compo => Census data

releasing too many aggregates alllow for a successful membership attack
partial knowledge can lead to disclosure by membership attcks

Reconstruction -> linkage -> re-identification
Membership -> value disclosure (by inference) no need of re-identification

### Anonymization vs Pseudonymization

Anonymization = transformation of data in a way such that people can no longer be identified => impossible to guarantee absolutely

Pseudonymization = processing of personal data in such a way that data can no longer be attributed to a specific data subject (without the use of additional)


## Tools

- *OpenDP*
- *DP-SDG*


- `env | grep GIT` : to get GIT environment variables 
- `env | grep AWS` : to get AWS environment variables (credentials to connect to s3 storage)

`python -m http.server -d slides/ -b 0.0.0.0 5000` : to publish slides on a url (enable before diffusion on several )
- 0.0.0.0 (local url)
- 5000 (port)


## PETS

How to choose the right combination f input and pricy output.

- where and why PETS can be used by NSO
- high level understanding 
- how to find relevant combination of PETs


### Definition

PETs = tools that permit data processing and analysis while protecting the confidentiality of collected data or derived data throughout the data flow


Two types of techno: Input Privacy techno vs Output Privacy techno

Information flow and stakeholders :
Source data (people/companies) -> collected by an input party (NSI eg) -> transfered by computing parties (computing services, data centers, sovereign or cloud) -> analyzed and disseminated to the result party  (public society, legally bounds)

Ensure confidentiality along this flow of info.

*Input privacy techno*: multiple parties can execute computation tasks without exposing the input data to each other (eg Security)

*Output privacy techno*: modify the output that produces an output to limit disclosure afetr (eg: SDC)

Who do you trust ?

Input parties / Computing arties / Results parties ?

- Output privacy: No trust on results parties but trust for computing and Input parties (classical SDC for NSI)
- The source does not trust the other parties (ex personal mobile data)
- Input privacy: the input privacy doesn't trust the computing parties (for example release data on cloud services): make sure that the computing party can't attack the data

- multiple parties : make sure that each party can't see the other's data but compute on both
(cas de RESIL)

Output privacy: trust scheme for public administration, but mmake sure that the result parties can't attack the data. 

What is THE solution ? privacy is complex / context dependent => no silver bullet PET.

### Input privacy 

More security topic

#### Secure enclaves 

Input -> encrypted transmission to the compute party -> decrypted when on the storage -> computation -> storage -> encryption for transfer to the input party 

The storage is also encrypted: the only access to data is only via the computation.

The Secure enclave is composed by the storage and computation party that are totally isolated to the input party.

ensures:
- input privacy
- code privacy
- code assurance
- all algo can be performed
- easy to deploy

But:
- truts in the hardware (but possibility of physical attacks)
- no formal privacy security guarantee

PET Guide of UN

Example: Different Mobile Network Providers don't trust each other but use an isolated computation environment that the ministry of tourism can used to publish some results (Indonesia)

#### Homomorphic encryption

The step of decryption is skipped and an end to end encryption is preferred.
The data and the operation on them are protected.

ensures:
- formal guarantees against security breach
- allowing to external computing 

limits:
- computational costs are exponential (=> limited on simple calculations )

Example from Canada:
Stat Can performs some model with Homorphic encryption : > 2500 fois plus de temps

Very lively research on this field

#### Secure Multi party Data Analysis Pipeline

cryptographic techno that allows two or more mutually distrusting parties to compute an agreed function

Ensures:
- mature techno 
- formal proofs of security
- very active community

Limits:
- susceptible of collusion
- expert knowledge needed for each algo
- often private companies owned the solution (not so open source)


Example: from US
Two national data providers on students data (they can't share the data to each other by law) : use security multiparty  to make statistics on the intersection of the two datasets.

#### Distributed Learning / Federal Learnin

One ML algo to be trained from different sources data 
train the data without sharing the data 

ensures:
- no need to share

limits:
- do not prevent personal data leak through trained ML
- trained model with federal learning are less performant


### Output privacy 

Differential Privacy = framework to transform the data while monitoring confidentiality/utility trade-off by randomizing the output of an algo

ensures:
- formal mathematical guarantee on disclosure risk
- many scientific works on DP-algo

BUT:
- choose the noise scale
- production implementation could be difficult (need of tailored standard solutions)

Example: LOMAS used to make experimentation 
Federal IT infrastructure : Swiss Researchers provide analysis plan applied directly on the real data but the results are DP protected. (need DP algo available)


#### Local DP

The DP is applied directly on the data collected (Randomized Response)

Ensures:
- data at individual level cannot be used against its owner
- early protection reduces the need for input privacy

Example: Mobile DATA (US cloud act): data partially randomized
Apple: quicktype = learns words that users type more often
The data sent are not raw data but partially randomized 
Health Kit App uses also local DP.


#### Synthetic Data

1. Simulate Dataset with the same data type (reproduce only the metadata of the dataset) => Dummy dataset
2. Create a new dataset with similar statistical properties without revealing information 

ensures:
- produce confidential microdata (pas sûr)
- dissemination and usability readiness

but:
- not formal proof 
- one synthetic dataset 

Example UH 2021 Census
Dummy Census to test their pipelines (Synthetizer + Differential Privacy)
marginals are computed and privatized by DP.

### Put everything together

Pet federated ML (-> Eurostat)
Joconde Project


## Differential Privacy

Membership / Inference Attack 

Abolute anonymaization is a broken promise
We can use the likelihood of data

Uncertain identification cannot be prevented but can be made uncertain !
Even uncertain identification disclosure can be harmful because of inference attack => limit the ability to infer sensitive data

### Definition and Properties of DP

vulnerability of conventional disclosure control techniques to linkage and reconstruction and membership attacks

#### Objectives of a successful SDC technique

1. indivdual data protection
2. Guarantees independent of auxiliary information and techncal capabilities
3. Cumulative risk quantification to decide when to stop disclosing information

=> DP satisfies the three criteria (ils sont faits pour ça)

#### Randomizer computation

A layer is added to the information flow = randomization

#### DP principle

All DP private algo are random  BUT not all random algo are DP
DP rand.: result of query + Noise
Privacy loss parameter to do the privacy / utility trade-off.


*Adjacent Databases*
Math definition (likelihood ratio is bounded by $e^\varepsilon$) => first crireria satisfied (individual data protection) => quantify how much statistical on adjacent databases can be distinguished
From DP perspective, the randomness is only on the noise.
So it is conditionally to the data collected.

represntation of the likelihood ratio as the ratio of the noise density. 
DP controls the maximal distinguisability power between these two models of random variables. 


*Post-processing*: the DP guarantees are preserved to any post processing analysis even using auxiliary information. => Second criteria
Worst case scenario = know everything but the target.

*Composition*: overall DP budget must be tracked => third criteria
independance comes from independent noise addition

### Laplacian Mechanism

Scale of the noise has to be equal sensitivity / epsilon.

Sensititivity = max difference between query on D and query on D' (D and D' adjacent)
The scale of the noise is adapted both to the nature of the query and the nature of the data.

Example: query of mean on binary values => sensitivity = 1/n where n is the number of individuals.
=> practical to release percentages.













### Laplace Noise Addition


