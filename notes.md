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





