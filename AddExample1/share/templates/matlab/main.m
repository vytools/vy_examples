% DONT MODIFY THIS FILE!
% This file:
%  1. loads some test values 
%  2. executes your "array" function on those values
%  3. stores the result
function main()
  addpath('/engine/jsonlab');
  vt = vy_tests();
  input_json = getenv('input_json');
  data = loadjson(fileread(input_json));
  if isfield(data,'problems')
    for ii = 1:length(data.problems)
      a = getif(data.problems{ii}.inputs,"a",-1.0);
      b = getif(data.problems{ii}.inputs,"b",1.0);
      c = add(a, b);
      if isfield(data.problems{ii},'outputs')
        data.problems{ii}.outputs = vt.grade_problem(data.problems{ii}.outputs, "c", c);
      endif
    endfor
  endif  
  write_json(data)
endfunction

function x = getif(strct,field,value)
  if isfield(strct,field)
    x = strct.(field);
  else
    x = value;
  endif
endfunction

function write_json(data)
  output_json = getenv('output_json');
  fid = fopen(output_json,'w');
  fprintf(fid,'%s',savejson('',data));
  fclose(fid);
endfunction