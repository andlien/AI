package main;

import java.util.ArrayList;
import java.util.HashMap;

import main.Assignment5.CSP;
import main.Assignment5.CSP.Pair;
import main.Assignment5.VariablesToDomainsMapping;

public class Hei {
	
	//static ArrayList<int[]> constraints;
	
	
	//static ArrayList<ArrayList<Integer>> variables;
	
	static ArrayList<String> variables;
	
	static HashMap<String, HashMap<String, ArrayList<Pair<String>>>> constraints;
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//System.out.println("Jeg fungerer!");
		CSP sudoko = Assignment5.createSudokuCSP("src/main/veryhard.txt");
		Assignment5.printSudokuSolution(sudoko.backtrackingSearch());
		/*
		
		System.out.println("variables: " + sudoko.variables);
		System.out.println("domains: " + sudoko.domains);
		//System.out.println("constraints: " + sudoko.constraints);
		
		System.out.println(" ");
		
		CSP australia = Assignment5.createMapColoringCSP();
		
		variables = australia.variables;
		VariablesToDomainsMapping domains = australia.domains;
		constraints = australia.constraints;
		
		String removed1 = domains.get("WA").remove(0);
		System.out.println("Removed " + removed1);
		removed1 = domains.get("WA").remove(0);
		System.out.println("Removed " + removed1);
		removed1 = domains.get("WA").remove(0);
		System.out.println("Removed " + removed1);
		
		//australia.constraints.
		for (int i = 0; i < australia.variables.size(); i++) {
			String string = australia.variables.get(i);
			//System.out.println(string + ": " + australia.domains.get(string));
			
			for (int i2 = 0; i2 < australia.variables.size(); i2++) {
				String naboStreng = australia.variables.get(i2);
				ArrayList<Pair<String>> nabo = australia.constraints.get(string).get(naboStreng);
				
				if(nabo != null){
					//System.out.println(naboStreng);
					//System.out.println(nabo);
					revise(domains, string, naboStreng);
					System.out.println("-------");
					
				}
			}
			
		}
		*/
		/*
		
		variables = new ArrayList<ArrayList<Integer>>();
		
		ArrayList<Integer> xVar = new ArrayList<Integer>();
		xVar.add(1);
		xVar.add(2);
		xVar.add(3);
		
		ArrayList<Integer> yVar = new ArrayList<Integer>();
		yVar.add(3);
		yVar.add(4);
		yVar.add(5);
		yVar.add(6);
		
		variables.add(xVar);
		variables.add(yVar);
		variables.add(xVar);
		
		constraints = new ArrayList<int[]> ();
		constraints.add(new int[]{1,3});
		constraints.add(new int[]{1,5});
		constraints.add(new int[]{3,3});
		constraints.add(new int[]{3,6});
		
		for (int di = 0; di < variables.size() -1; di++) {
			ArrayList<Integer> x = variables.get(di);
			ArrayList<Integer> y = variables.get(di + 1);
				
			
			ArrayList<int[]> worklist = new ArrayList<int[]> ();
			for (int i = 0; i < x.size(); i++) {
				for (int j = 0; j < y.size(); j++) {
					int[] temp = new int[2];
					temp[0] = x.get(i);
					temp[1] = y.get(j);
					worklist.add(temp);
					System.out.println(temp[0] + " og " + temp[1]);
					temp[1] = x.get(i);
					temp[0] = y.get(j);
					worklist.add(temp);
					System.out.println(temp[0] + " og " + temp[1]);
				}
			}
			int[] temp = worklist.remove(0);
			int x1 = temp[0];
			int y1 = temp[1];
			if(arcReduce(x,y)){
				if(x.size() < 1) System.out.println("Dette gar ikke");
			}

		}
		System.out.println(xVar);
		System.out.println(yVar);
		*/
	}//end main
	
	public static boolean arcReduce(ArrayList<Integer> x, ArrayList<Integer> y){
		boolean revised = false;
		for (int i = 0; i < x.size(); i++) {
			boolean matchFound = false;
			int vx = x.get(i);
			for (int j = 0; j < y.size(); j++) {
				int vy = y.get(j);
				
				//Revised
				for (int k = 0; k < constraints.size(); k++) {
					//if(vx == x1 && vy == y1){
						//if(constraints.get(k)[0] == vx && constraints.get(k)[1] == vy) matchFound = true;
						//if(constraints.get(k)[1] == vx && constraints.get(k)[0] == vy) matchFound = true;						
					//}
				}
				
			}
			if(!matchFound){
				System.out.println(vx + " finnes ikke");
				x.remove(i);
				revised = true;
			}
		}
		
		return revised;
	}
	
	public static boolean revise(VariablesToDomainsMapping assignment, String i, String j) {
		System.out.println("revise (): i=" + i + " and j=" + j );
		boolean revised = false;
		for (int i2 = 0; i2 < assignment.get(i).size(); i2++) {
			String colorI = assignment.get(i).get(i2);
			//System.out.println("Color: " + colorI);
			
			boolean domainChanged = false;
			
			for (int j2 = 0; j2 < assignment.get(j).size(); j2++) {
				String colorJ = assignment.get(j).get(j2);
				//System.out.println("	Color: " + colorJ);
				
				
				for (int k = 0; k < constraints.get(i).get(j).size(); k++) {
					Pair pair = constraints.get(i).get(j).get(k);
					//System.out.println(" 		Constraint: " + constraints.get(i).get(j).get(k));
					if(colorI == pair.x && colorJ == pair.y){
						//System.out.println("			Match");
						domainChanged = true;
					}
				}
				
			}
			
			//if(domainChanged) System.out.println("Match found. Domain unchanged");
			if(!domainChanged){
				System.out.println("Match not found. Deleting " + colorI + " from " + i);
				assignment.get(i).remove(i2);
				System.out.println("Updated domain: " + assignment.get(i));
				System.out.println(" ");
				revised = true;
			}
			
		}
		return revised;
	}

}//end class
