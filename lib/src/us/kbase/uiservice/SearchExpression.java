
package us.kbase.uiservice;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: SearchExpression</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "op",
    "args"
})
public class SearchExpression {

    @JsonProperty("op")
    private String op;
    @JsonProperty("args")
    private List<SearchArg> args;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("op")
    public String getOp() {
        return op;
    }

    @JsonProperty("op")
    public void setOp(String op) {
        this.op = op;
    }

    public SearchExpression withOp(String op) {
        this.op = op;
        return this;
    }

    @JsonProperty("args")
    public List<SearchArg> getArgs() {
        return args;
    }

    @JsonProperty("args")
    public void setArgs(List<SearchArg> args) {
        this.args = args;
    }

    public SearchExpression withArgs(List<SearchArg> args) {
        this.args = args;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((("SearchExpression"+" [op=")+ op)+", args=")+ args)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
