package edu.uwf.kennethdale.scavenger_client;

import android.content.Context;
import android.widget.ArrayAdapter;
import android.widget.Spinner;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;

public class Utility {
    public void populateSpinner(Context thisContext, Spinner spinner, String route, String attribute){
        String responseText = "";

        HttpGetRequest getRequest = new HttpGetRequest();
        try {
            responseText = getRequest.execute("http://188.166.97.39:8080/" + route).get();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }

        List<String> items = new ArrayList<String>();
        try {
            JSONArray array = new JSONArray(responseText);

            for (int i = 0; i < array.length(); i++){
                JSONObject resp = array.getJSONObject(i);
                items.add(resp.getString(attribute));
            }
        } catch(JSONException e){
            e.printStackTrace();
        }

        ArrayAdapter<String> dataAdapter = new ArrayAdapter<String>(thisContext, android.R.layout.simple_spinner_item, items);
        dataAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(dataAdapter);
    }
}
