
package us.kbase.uiservice;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: CheckHTMLURLParams</p>
 * <pre>
 * Check html url
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "url",
    "timeout"
})
public class CheckHTMLURLParams {

    @JsonProperty("url")
    private String url;
    @JsonProperty("timeout")
    private Long timeout;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("url")
    public String getUrl() {
        return url;
    }

    @JsonProperty("url")
    public void setUrl(String url) {
        this.url = url;
    }

    public CheckHTMLURLParams withUrl(String url) {
        this.url = url;
        return this;
    }

    @JsonProperty("timeout")
    public Long getTimeout() {
        return timeout;
    }

    @JsonProperty("timeout")
    public void setTimeout(Long timeout) {
        this.timeout = timeout;
    }

    public CheckHTMLURLParams withTimeout(Long timeout) {
        this.timeout = timeout;
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
        return ((((((("CheckHTMLURLParams"+" [url=")+ url)+", timeout=")+ timeout)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
