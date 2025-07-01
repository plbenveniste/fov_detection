import nibabel as nib # type: ignore
file_path = "/Users/nathanbenveniste/Desktop/Coding Projects/Python Projects/AI_Internship/seg_img_step2_output.nii.gz"
img = nib.load(file_path)
data = img.get_fdata()
print(f"Dimensions : {data.shape}")
# ici on print les valeurs uniques
unique_values = set(data.flatten())
print(f"Unique values in the image: {unique_values}")
# on détermine quels types de vertèbres sont présents
C,T,L = False,False,False
# Cervical vertebrae: 11-17
# Thoracic vertebrae: 21-32
# Lumbar vertebrae: 41-45
# On vérifie si les valeurs uniques contiennent des vertèbres cervicales, thoraciques ou lombaires
for x in unique_values:
    if 11<= x <= 17:
        C = True
    if 21<= x <= 32:
        T = True
    if 41<= x <= 45:
        L = True
print(f"Cervical vertebrae present: {C}")
print(f"Thoracic vertebrae present: {T}")
print(f"Lumbar vertebrae present: {L}")

#print ,modif
