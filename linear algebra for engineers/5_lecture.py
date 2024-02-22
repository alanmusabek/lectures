# arbitrary nonempty sets
A_set = [1, 2, 3, 4, 5] # <- the domain of the mapping
B_set = [25, 30, 10, 12, 11] # <- target set


map_ = {
    A_set[0]: B_set[4], # B_set[4], is a unique element of B, e.g. image of a
    A_set[1]: B_set[2],
    A_set[2]: B_set[1],
    A_set[3]: B_set[0],
    A_set[4]: B_set[3]
}

print("Map is a collection of assignments to each unique element of A, element from B")
print("f: A -> B")
print(map_)
print("The IMAGE is a unique element b,", B_set[4],"from set B that is assigned to an element a from set A,", A_set[0])

# linear_mapping or homomorphism
def linear_mapping(V):
    return 0


V = [[1, 2, 3], [2, 3, 4]]
U = [[1], [2], [3], [4]]
linear_mapping = {
    "[1]": V[0],
    "[2]": V[1],
    "[3]": [3, 5, 7],
    "[4]": [3, 6, 9]
}
# It is over simplified version.
# linear mapping is valid if for any vector v1, v2 from V, F(v1 + v2) = F(v1) + F(v2)
# and if for any scalar lambda and v from V this statement is valid F(lambdav) = lambdaF(v)

#first check
new_vector_1 = [V[0][0] + V[1][0],V[0][1] + V[1][1], V[0][2] + V[1][2]]
new_vector_2 = [linear_mapping["[1]"][0] + linear_mapping["[2]"][0], linear_mapping["[1]"][1] + linear_mapping["[2]"][1], linear_mapping["[1]"][2] + linear_mapping["[2]"][2]]
lambda_vector_v = [3*V[0][0], 3*V[0][1], 3*V[0][2]]
lambda_vector_mapping = [3 * linear_mapping["[1]"][0],3 * linear_mapping["[1]"][1],3 * linear_mapping["[1]"][2]]

print(new_vector_1 == new_vector_2)
print(lambda_vector_v == lambda_vector_mapping)

#All conditions are ment, thus this is linear mapping. However V and U vector spaces must consist from every possible vector in K field. I used oversimplified version of the vector space.
#This is for illustration purposes.