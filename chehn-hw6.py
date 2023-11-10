from pymongo import MongoClient as mc
import argparse as ap

# MongoClient startup
client = mc('localhost', 27017)
db = client['hw6']
collection = db['business']

def closest_businesses(lat, lon):
    query = { "location": { "$near": { "$geometry": { "type": "Point",  "coordinates": [ (float)(lon), (float)(lat) ] }} } }
    docs = collection.find(query).limit(3)
    for doc in docs:
        print('-------------------')
        print(doc['name'] + ', ', doc['address'] + ', ', doc['city'] + ', ', doc['state'] + ', Categories: ', doc['categories'] + ', ', (str)(doc['stars']) + ' stars, ', (str)(doc['review_count']) + ' reviews.')
        print('-------------------')
    return

def submit_review(id):
    query = { 'business_id': id }
    sb = collection.find_one(query)
    if not sb:
        print('No business found with that ID. Please try again.')
        return
        
    star_rating = input('Star rating for this business (1-5):')
    if isinstance(star_rating, float):
        print('Invalid star rating. Please enter a number between 1 and 5.')
    if (float)(star_rating) < 1 or (float)(star_rating) > 5:
        print('Invalid star rating. Please enter a number between 1 and 5.')

    review = { "stars" : star_rating }
    submission = db['reviews'].insert_one(review)

    print('Review submitted successfully. Review ID: ' + (str)(submission.inserted_id))

    new_score = sb['stars'] * sb['review_count'] + (float)(star_rating)
    updated_rating = new_score / (sb['review_count'] + 1)

    result = collection.update_one({ "business_id": id }, {"$set": { "stars" : updated_rating }, "$inc" : {'review_count' : 1}} )
    if result.modified_count == 1:
        print('Business star rating updated successfully. ' + (str)(result.modified_count) + ' document updated.')
    else:
        print('More than one business was found with that ID. Their star ratings have all been updated. Please check your database.')
    return

if __name__ == '__main__':
    parser = ap.ArgumentParser(
                    prog='HW6 MongoDB CLI',
                    description='Provides functionality to interact with the business collection in the hw6 database for ECE:5845.',
                    epilog='More details on the program can be found in the README.')

    # Create arguments for CLI
    parser.add_argument("function", help="The function you would like to execute. Options are: closest_businesses, submit_review")
    parser.add_argument("-lat", "--latitude", dest='lat', required=False)
    parser.add_argument("-lon", "--longitude", dest='lon', required=False)
    parser.add_argument("-id", "--business_id", dest='id', required=False)

    args = parser.parse_args()

    # Based on the function the user wants to run, execute respective method.
    match args.function:
        case "closest_businesses":
            print('Executing -> List three closest businesses to lat/lon.')
            closest_businesses(args.lat, args.lon)
        case "submit_review":
            print('Executing -> Submit a review for a business given its ID.')
            submit_review(args.id)