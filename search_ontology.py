from owlready2 import *
import os
import types
import json
import csv
path = os.path.dirname(os.path.abspath(__file__))
onto = get_ontology(path + "/ontology19.owl").load()


#############  To convert a "name with space" to "name with underscore #########
#                                                                              #
################################################################################

def ClassName(name):
  if name.count(' ') >= 1:
    new_class_name = name.replace(' ','_')
  else:
    new_class_name = name
  return new_class_name

############# End of "To convert a "name with space" to "name with underscore" ##########
#                                                                                       #
#########################################################################################


#############  To convert a "name with underscore" "name with space" ###########
#                                                                              #
################################################################################

def ReverseClassName(name):
  if name.count('_') >= 1:
    new_class_name = name.replace('_',' ')
  else:
    new_class_name = name
  return new_class_name

############# End of "To convert a "name with underscore" "name with space"" ############
#                                                                                       #
#########################################################################################



#############  Return all the instances of direct parent     ####### ###########
#                                                                              #
################################################################################

def Individuals(direct_parent):
  print(direct_parent)
  intance_classes = onto[direct_parent].instances()
  compound_names = [i.name for i in intance_classes]
  # print("returned all the compounds:{}".format(compound_names))
  return compound_names


############# End of "Return all the instances of direct parent "" ######################
#                                                                                       #
#########################################################################################



#############  Return all the terms for a subont    ####### ###########
#                                                                              #
################################################################################

def IndividualTerms(converted_sub_ontology,compound):
  terms = []
  # print("received converted_sub_ontology:{} to calculate terms for:{}".format(converted_sub_ontology,compound))
  if converted_sub_ontology == "Indirect_biological_role":
    temp_terms = onto[compound].has_for_indrect_biological_role
    if temp_terms:
      for t in temp_terms:
        terms.append(t.name)
  elif converted_sub_ontology == "Industrial_process":
    temp_terms = onto[compound].has_for_industrial_process
    if temp_terms:
      for t in temp_terms:
        terms.append(t.name)
  elif converted_sub_ontology == "Industrial_application":
    temp_terms = onto[compound].has_for_industrial_application
    if temp_terms:
      for t in temp_terms:
        terms.append(t.name)
  # print("terms for the compound {} and sub_ont : {} found:{}".format(compound,converted_sub_ontology,terms))
  return terms


############# End of "Return all the terms for a subon"" ######################
#                                                                                       #
#########################################################################################


#############  Return all the class hierarchy for a compoun    ####### ###########
#                                                                              #
################################################################################

def ClassHierarchy(converted_direct_parent,temp_comp):
  ancestors = onto[converted_direct_parent].ancestors()
  d_p = onto[converted_direct_parent].name
  temp_comp["DirectParent"] = d_p
  sub_class = onto[d_p].is_a[0].name
  temp_comp["SubClass"] = sub_class
  if len(ancestors)-3 == 5: 
    klass = onto[sub_class].is_a[0].name 
    temp_comp["Class"] = klass
  else:
    klass = sub_class
    temp_comp["Class"] = sub_class
  supe_class = onto[klass].is_a[0].name
  temp_comp["SuperClass"] = supe_class
  Kingdom = onto[supe_class].is_a[0].name
  temp_comp["Kingdom"] = Kingdom 
  return temp_comp


############# End of "Return all the class hierarchy for a compoun"" ####################
#                                                                                       #
#########################################################################################

#############  Return all the term hierarchy for a compound    ####### ###########
#                                                                              #
################################################################################

def KlassHierarchy(converted_direct_parent,temp_comp):
  ancestors = onto[converted_direct_parent].ancestors()
  d_p = onto[converted_direct_parent].name
  temp_comp["DirectParent"] = d_p
  sub_class = onto[d_p].is_a[0].name
  temp_comp["SubClass"] = sub_class
  if len(ancestors)-3 == 5: 
    klass = onto[sub_class].is_a[0].name 
    temp_comp["Class"] = klass
  else:
    klass = sub_class
    temp_comp["Class"] = sub_class
  supe_class = onto[klass].is_a[0].name
  temp_comp["SuperClass"] = supe_class
  Kingdom = onto[supe_class].is_a[0].name
  temp_comp["Kingdom"] = Kingdom 
  return temp_comp


############# End of "Return all the term hierarchy for a compound"" ####################
#                                                                                       #
#########################################################################################

#############  Return all the term hierarchy for a term    ####### ###########
#                                                                              #
################################################################################

def TermHierarchy(each_term,temp_term_hierarchy):
  control_var = onto[each_term].is_a[0].name
  temp_hierarchy_values = []
  while (control_var != "StaticTerm"):
    temp_hierarchy_values.append(control_var)
    control_var = onto[control_var].is_a[0].name
  temp_term_hierarchy["Hierarchy"] = temp_hierarchy_values
  return temp_term_hierarchy


############# End of "Return all the term hierarchy for a term"" ####################
#                                                                                       #
#########################################################################################
def run_ontology_search(data):
  mw_from = data['mw_from'][0]
  mw_to = data['mw_to'][0]
  logp_from = data['logp_from'][0]
  logp_to = data['logp_to'][0]
  subont1 = data['subont1'][0]
  # subont2 = data['subont2'][0]
  subont3 = data['subont3'][0]
  term1 = data['term1'][0]
  # term2 = data['term2'][0]
  term3 = data['term3'][0]
  klass = data['klass'][0]
  sub_ontologies = ["Industrial process", "Industrial application", "Indirect biological role"]
#   print("###########################################")
#   print("THIS IS AN ALTERNATE APPROACH OF GUI\t")
#   print("###########################################")
#   print("Provide molecular weight in range:\n")
#   molecular_weight_from = input("From:\t")    #### conver it to float later
#   molecular_weight_to = input("To:\t")
#   # print("you have put m_w from:{} to: {}".format(molecular_weight_from,molecular_weight_to))    #### conver it to float later
#   print("\nProvide LogP weight in range:\n")
#   logp_from = input("From:\t")    #### conver it to float later
#   logp_to = input("To:\t")    #### conver it to float later
#   # print("you have put logp from:{} to: {}".format(logp_from,logp_to))
#   sub_ontologies = ["Industrial process", "Industrial application", "Indirect biological role"]
#   terms_idustrial_process = ["Leaching","metallurgical process","Petroleum processing","chelation","Desalination","Desalination","Water purification","Water disinfection","ammonia production","Distillation","Reverse Osmosis","Sedimentation","Filtration","Disinfection","Chlorine dioxide disinfection","Chloramine disinfection","Ozone disinfection","Ultraviolet disinfection","Gamma radiation","Water fluoridation","Water conditioning","Bioremediation","Fermentation","combustion"]
#   terms_idustrial_application = ["Algicide","Nematicide","Feed Additive","Fertiliser","Insect Attractant","Plant growth regulator","Ripening agent","Fertilizer","Herbicide","Insect repellent","Insecticide","Acaricide","Aphidicide","Biocide","Horticultural Spray Oil","Pesticide","Fumigant","Adhesive","Flame retardant","Acidulant","Flavor Enhancer","Foam Stabilizer","Acidity Regulator","Baking agent","Color Retention Agent","Firming Agent","Flavor Solvent","Flavoring Agent","Food additive","Food color","Food preservative","Improving Agent","Nutritional supplement","Packaging Gas","Raising agent","Resolving Agent","Seasoning","Sweetener","Thickening Agent","Carrier","Sequestrant","Fragrance Component","Glazing Agent","Probiotic","Anticaking agent","electrolyte replenisher","enzyme replacement agent","Prebiotic","Deodorant","Hair conditioner","Hair products","Lipstick","Lotion","Makeup","Moisturizer","mouthwash","Perfume","Shampoo","Shaving cream","Soap","Toothpaste","Wet wipes","UV filter","Anti AIDS","Antiadenoviral","Antiflu agent","Antimeasles","Antipapillomic","Antipoliomyelitic","Antirabies","Antiretroviral","Antirhinoviral","Antishingles","Antivaccinia","Ascaricide","Vermifuge","Anticytomegalovirus","AntiEpstein-Barr virus","Anticancer agent","Anticarcinogenic","Anticarcinomic","Antihepatocarcinogenic","Antileukemic","Antimelanogenic","Antimelanomic","Antimetastatic","Antineoplastic","Antitumor","Antitumor promoter","Cancer preventive","Carcinostatic","chemopreventive","Antiadenomic","Antihepatoadenomic","Antihepatomic","Antiprostatadenomic","Antisarcomic","Antiatherotic","Antiarrythmic","Antiatherogenic","Antiatherosclerotic"]
#   terms_indirect_biological_role = ["Allergen","amnesigenic","Cardiotoxin","cerebrotoxic","cyanotoxin","embryotoxic","endocrine disrupting","enterotoxic","fetotoxic","Genotoxin","hepatomegalic","Hepatotoxin","Lupus generating","marine biotoxin","mycotoxin","Nephrotoxin","Neurotoxin","pancreatoxic","phytotoxin","poison","pulmonotoxic","Reprotoxic","respirotoxic","toxin","uremic toxin","venom","Xenobiotic","Carcinogen","Cytotoxin","Mutagen","Teratogen","Osteotoxin","Renal toxin","Immunotoxin","Metabotoxin","Acidogen","Diabetogen","Atherogen","Mitochondrial toxin","Arthritogen","Phototoxin"]
#   print("Select two Sub-ontologies:(Example:{})".format(sub_ontologies))
#   sub_ontology1 = input("Sub-ontology 1:\t")
#   sub_ontology2 = input("Sub-ontology 2:\t")
#   # print("you have put sunbontology from:{} to: {}".format(sub_ontology1,sub_ontology2))
#   print("Provide one term per Sub-ontology:")
#   term_sub_ontology1 = input("Term for Sub-Ontology 1:\t")
#   term_sub_ontology2 = input("Term for Sub-Ontology 2:\t")
#   # print("you have provided  term1:{} term2: {}".format(term_sub_ontology1,term_sub_ontology2))
#   # classes = ["A","B"]
#   #print("Provide the chemical class:(Example:{})".format(classes))
#   print("Provide the chemical class:")
#   direct_parent = input("Chemical Class:\t")

# ##################################################
# #After getting input load the ontology and search#
# ##################################################
# # load is done at the beginning and the variable is "onto"\


  m_w_control = False
  logp_control = False
  onto_control = False
  term1_control = False
  term2_control = False
  converted_direct_parent = ClassName(klass)
  compounds_in_chemical_class = Individuals(converted_direct_parent)
  list_of_the_compounds = []
  list_of_the_hierarchy_for_terms = []
  for compound in compounds_in_chemical_class:
    # print("Started with compound:{}".format(compound))
    temp_comp = {}
    temp_hierarchy_for_terms = {}
    m_w = onto[compound].has_for_molecula_weight[0].name
    # print("Got m_w:{}".format(m_w))
    if round(float(m_w),3) >= float(mw_from) and  round(float(m_w),3) <= float(mw_to):
      m_w_control = True
      # print("m_w_contro set to:{}".format(m_w_control))
    else:
      m_w_control = False
      # print("m_w_contro set to:{}".format(m_w_control))
    logp = onto[compound].has_for_logp[0].name
    # print("Got logp for the compound:{}".format(logp))
    if round(float(logp),3) >= float(logp_from) and  round(float(logp),3) <= float(logp_to) :
      logp_control = True
      # print("logp control set to:{}".format(logp_control))
    else:
      logp_control = False
      # print("logp control set to:{}".format(logp_control))
    converted_sub_ontology1 = ClassName(subont1)
    converted_sub_ontology2 = ClassName(subont3)
    term1 = term1
    term2 = term3
    terms_for_compounds_in_subont_1 = IndividualTerms(converted_sub_ontology1,compound) # it is giving me all the terms associated with that compound for sub_ont1
    terms_for_compounds_in_subont_2 = IndividualTerms(converted_sub_ontology2,compound) # it is giving me all the terms associated with that compound for sub_ont2
    if term1 in terms_for_compounds_in_subont_1: 
      term1_control = True
      # print("term1_control  set to:{}".format(term1_control))
    else:
      term1_control = False
      # print("term1_control  set to:{}".format(term1_control))
    if term2 in terms_for_compounds_in_subont_2: 
      term2_control = True
      # print("term2_control  set to:{}".format(term2_control))
    else:
      term2_control = False
      # print("term2_control  set to:{}".format(term2_control))
    if m_w_control == True and logp_control == True and term1_control == True:
      # print("found compound : {}".format(compound))
      temp_comp["CompoundName"] = compound
      temp_comp["MolecularWeight"] = m_w
      temp_comp["LogP"] = logp
      temp_comp["DatabaseID"] = onto[compound].has_for_database_ID[0].name
      KlassHierarchy(converted_direct_parent,temp_comp)
      total_sub_ont_from_input = []
      total_sub_ont_from_input.append(subont1)
      total_sub_ont_from_input.append(subont3)
      remaining_sub_ontology = list(set(sub_ontologies).difference(total_sub_ont_from_input))
      converted_remaining_sub_ontology = ClassName(remaining_sub_ontology)
      terms_for_remaining_sub_ont = IndividualTerms(converted_remaining_sub_ontology,compound)
      # print("terms for sub_ont1:{}".format(terms_for_compounds_in_subont_1))
      # print("terms for sub_ont2:{}".format(terms_for_compounds_in_subont_2))
      # print("terms for sub_ont3:{}".format(terms_for_remaining_sub_ont))
      total_terms_for_the_compound = terms_for_compounds_in_subont_1 + terms_for_compounds_in_subont_2 + terms_for_remaining_sub_ont
      # print("now total terms:{}".format(total_terms_for_the_compound))
      temp_comp["Terms"] = total_terms_for_the_compound
      list_of_the_compounds.append(temp_comp)
      for each_term in total_terms_for_the_compound:
        temp_term_hierarchy = {}
        temp_term_hierarchy["term"] = each_term
        TermHierarchy(each_term,temp_term_hierarchy)
        list_of_the_hierarchy_for_terms.append(temp_term_hierarchy)
  #print("compounds:\n{}".format(list_of_the_compounds))
  #print("terms:\n{}".format(list_of_the_hierarchy_for_terms))

  ####### print the final result ####################################
  ###################################################################

  print("\n################# SEARCH   RESULTS ###########################\n\n")
  print("TOTAL NUMBER OF COMPOUND FOUND IN DATABASE:{}".format(len(list_of_the_compounds)))
  final_d = {}
  for each_com in list_of_the_compounds:
    final_d['compound'] = {}
    final_d['compound']['database_id'] = each_com["DatabaseID"]
    final_d['compound']['compound_name'] = each_com["CompoundName"]
    final_d['compound']["molecular_weight"] = each_com["MolecularWeight"]
    final_d['compound']["logp"] = each_com["LogP"]
    final_d['compound']['kingdom'] = each_com["Kingdom"]
    final_d['compound']['super_class'] = each_com["SuperClass"]
    final_d['compound']['class'] = each_com["Class"]
    final_d['compound']['sub_class'] = each_com["SubClass"]
    final_d['compound']['direct_parent'] = each_com["DirectParent"]
    # final_d['compound']['terms'] = each_com["Terms"]
    final_d['compound']['terms'] = {}
    
    print("\t\t\tCOMPOUND NAME : {}".format(each_com["CompoundName"]))
    print("Molecular Weight    : {}".format(each_com["MolecularWeight"]))
    print("LogP                : {}".format(each_com["LogP"]))
    print("Database ID         : {}".format(each_com["DatabaseID"]))
    print("Chemical Ontology:")
    print("\t\t\tKingdom")
    print("\t\t\t({})".format(ReverseClassName(each_com["Kingdom"])))
    print("\t\t\t|")
    print("\t\t\t|")
    print("\t\t\tSuper Class")
    print("\t\t\t({})".format(ReverseClassName(each_com["SuperClass"])))
    print("\t\t\t|")
    print("\t\t\t|")
    print("\t\t\tClass")
    print("\t\t\t({})".format(ReverseClassName(each_com["Class"])))
    print("\t\t\t|")
    print("\t\t\t|")
    print("\t\t\tSub Class")
    print("\t\t\t({})".format(ReverseClassName(each_com["SubClass"])))
    print("\t\t\t|")
    print("\t\t\t|")
    print("\t\t\tDirect Parent")
    print("\t\t\t({})".format(ReverseClassName(each_com["DirectParent"])))
    for term in list_of_the_hierarchy_for_terms:
      final_d['compound']['terms'][term["term"]] = []
      print("The compound is a:")
      print("\t\t\t{}".format(ReverseClassName(term["term"])))
      for hierarchy in term["Hierarchy"]:
        final_d['compound']['terms'][term["term"]].append(hierarchy)
        print("\t\t\t|")
        print("\t\t\twhich is in:{}".format(ReverseClassName(hierarchy)))
        
  # final_list = []
  # final_list.append(list_of_the_compounds)
  # final_list.append(list_of_the_hierarchy_for_terms)
  return final_d




    


  





