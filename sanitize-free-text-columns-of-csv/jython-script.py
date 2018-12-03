import sys
import traceback
from org.apache.commons.io import IOUtils
from org.apache.nifi.processor.io import StreamCallback
from org.python.core.util import StringUtil
from java.lang import Class
from java.io import BufferedReader
from java.io import InputStreamReader
from java.io import OutputStreamWriter


class TransformCallback(StreamCallback):
    def __init__(self):
        pass

    def process(self, input_stream, output_stream):

        try:
            writer = OutputStreamWriter(output_stream, "UTF-8")
            reader = BufferedReader(InputStreamReader(input_stream, "UTF-8"))
            line = reader.readLine()

            found_quote_flag = False
            while line != None:

                # Write the line always
                writer.write(line)

                # If there is an odd number of double quotes (free text field)
                # then there is a newline somewhere in one of the column fields.
                # Raise the flag to not add any newlines until we've found the matching 
                # line that contains an odd number of quotes
                if line.count('"') % 2 != 0:
                    found_quote_flag = not found_quote_flag

                if not found_quote_flag:
                    writer.write('\n')

                line = reader.readLine()

            writer.flush()
            writer.close()
            reader.close()
            
        except:
            traceback.print_exc(file=sys.stdout)
            raise


flowFile = session.get()
if flowFile != None:
    flowFile = session.write(flowFile, TransformCallback())

    # Finish by transferring the FlowFile to an output relationship
    session.transfer(flowFile, REL_SUCCESS)