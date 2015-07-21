/*
 *  Copyright (c) 2015, Parse, LLC. All rights reserved.
 *
 *  You are hereby granted a non-exclusive, worldwide, royalty-free license to use,
 *  copy, modify, and distribute this software in source code or binary form for use
 *  in connection with the web services and APIs provided by Parse.
 *
 *  As with any software that integrates with the Parse platform, your use of
 *  this software is subject to the Parse Terms of Service
 *  [https://www.parse.com/about/terms]. This copyright notice shall be
 *  included in all copies or substantial portions of the software.
 *
 *  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 *  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
 *  FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
 *  COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 *  IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 *  CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 *
 */

#include <stdio.h>
#include <parse.h>

void myPushCallback(ParseClient client, int error, const char *buffer) {
      if (error == 0 && buffer != NULL) {
              printf("received push: '%s'\n", buffer);
                }
}

int main(int argc, char *argv[]) {
    ParseClient client = parseInitialize("kKW7oJS0nwEG4V6f3LvYooU5BQxFnH6eZ9aS31A3", "9OYwyRgiH7g9rPAPYD7qq5wAYlBdLIvkz9c4UzwG");
    parseSendRequest(client, "POST", "/1/classes/TestObject", "{\"foo\":\"bar\"}", NULL);

    parseSetPushCallback(client, myPushCallback);
    parseStartPushService(client);
     
    parseRunPushLoop(client);

    return 0;
}

