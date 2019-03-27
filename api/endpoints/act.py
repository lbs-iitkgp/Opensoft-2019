from endpoints import *

@app.route('/act/<act_id>', methods=['GET'])
def act_metadata(act_id):
    act = mydb.mytable.find({"act_id":act_id})
    result ={
        'name': act['name'],
        'year': act['year'],
        'type': act['type'],
        'recent_version': {
            'id': act['recent_version_id'],
            'name': act['recent_version_name']
        },
        'abbreviation': act['abbreviation'] 
    }
    return jsonify(result)

@app.route('/act/<act_id>/sections', methods=['GET'])
def act_sections(act_id):
    result = []
    for section in mydb.mytable.find({"act_id":act_id}):
        section = {
                'section_id': section['section_id'],
                'section_text': section['section_text']
            }
        result.append(section)
    return jsonify(result)

@app.route('/act/<act_id>/section/<section_id>', methods=['GET'])
def act_section(act_id, section_id):
    sections = mydb.mytable.find({"act_id":act_id})
    section = mydb.sections[section_id].find({"section_id":section_id})
    result = {
       'section_id': section_id,
       'section_text': section['section_text'] 
    }
    return jsonify(result)


@app.route('/act/<act_id>/plot_line', methods=['GET'])
def act_line_distribution(act_id):
    # Iterate through each citer in neo4j
    #   Find citer's year from mongo
    #
    # 
    return('Hello')


@app.route('/act/<act_id>/cases', methods=['GET'])
def act_citations(act_id):
    # Fetch list of cases that cite this act from neo4j and return their details from mongodb as json
    return('Hello')
