from flask import Flask, request, jsonify,Blueprint

from utils.extract_keyword_util import find_companies

extract_keyword_routes=Blueprint('extract_keyword',__name__)
@extract_keyword_routes.route('/extract_keyword',methods=['post'])
def extract_keywords_route():
    paragraph = request.data.decode('utf-8')
    

    # Find the keywords using the paragraph
    keywords = find_companies(paragraph)

    # Return the keywords as JSON
    return jsonify({'keywords': keywords})

