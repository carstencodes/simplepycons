#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class HclIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hcl"

    @property
    def original_file_name(self) -> "str":
        return "hcl.svg"

    @property
    def title(self) -> "str":
        return "HCL"

    @property
    def primary_color(self) -> "str":
        return "#006BB6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HCL</title>
     <path d="M21.3968 10.4013l-1.0971
 2.4399H24l-.3435.7629H17.294l1.4331-3.2028zm-6.3985
 1.0896h2.4633c-.0152-.5377-.5358-.911-1.5672-1.0592-2.0348-.2994-4.2354-.1718-5.802.6934-1.2346.6859-1.329
 1.7176-.099 2.2232 1.0357.4218 3.2106.4656 4.767.201 1.0077-.1712
 1.7776-.502
 2.2093-.9974H14.454c-.3262.251-.7526.376-1.25.3804-1.4124.0094-1.5988-.4182-1.3525-.9106.293-.5801.9075-.8966
 1.8447-.9216.7381-.0199 1.1029.1436 1.3021.3908M0
 13.6067h2.604l.5578-1.2789h2.553l-.5732
 1.2771h2.635l1.4457-3.2031h-2.653l-.4769
 1.0807H3.5421l.4831-1.0807-2.5781-.0006Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
