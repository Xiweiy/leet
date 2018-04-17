class Solution(object):
    
    def getSubdomains(self, domainString):
        domainSplit = domainString.split(".")
        ndomain = len(domainSplit)
        return [".".join(domainSplit[i:]) for i in range(ndomain)]
    
    def subdomainVisits(self, cpdomains):
        domaindict = {}
        for x in cpdomains:
            value, domain = x.split()
            subdomains = self.getSubdomains(domain)
            for i in subdomains:
                if i in domaindict:
                    domaindict[i] += int(value)    ##convert to INT, otherwise will concatenate string
                else:
                    domaindict[i] = int(value)
        return [" ".join([str(domaindict[i]), i]) for i in domaindict]
