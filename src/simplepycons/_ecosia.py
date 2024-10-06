#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class EcosiaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ecosia"

    @property
    def original_file_name(self) -> "str":
        return "ecosia.svg"

    @property
    def title(self) -> "str":
        return "Ecosia"

    @property
    def primary_color(self) -> "str":
        return "#5DD25E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ecosia</title>
     <path d="m21.653 10.126.438 2.712h-.876zM24
 14.861l-1.009-5.722h-2.675l-1.01 5.722h1.583l.21-1.318h1.111l.209
 1.318zm-6.788
 0h1.682V9.139h-1.682zm-2.28-3.151c-.454-.173-.547-.274-.547-.431
 0-.199.168-.307.521-.307.488 0 1.027.166
 1.548.373V9.496c-.361-.299-1.009-.481-1.674-.481-1.153
 0-1.842.547-1.842 1.518 0 .845.438 1.243 1.439
 1.608l.37.133c.403.148.538.257.538.44 0 .14-.084.315-.505.315-.58
 0-1.279-.282-1.758-.539v2.065c.454.232 1.169.431 1.876.431 1.204 0
 1.893-.498 1.893-1.559 0-.722-.295-1.128-1.422-1.551zm-3.676.29c0
 .655-.261 1.037-.866 1.037-.606
 0-.867-.382-.867-1.037s.261-1.036.867-1.036c.605 0 .866.381.866
 1.036m-.867-2.985c-1.767 0-2.213 1.343-2.213 2.985 0 1.651.445 2.986
 2.212 2.986S12.6 13.651 12.6 12c0-1.642-.445-2.985-2.212-2.985zm-4.08
 2.031c.505 0 .883.149
 1.422.44V9.604c-.312-.34-.943-.589-1.573-.589-1.447 0-2.22.912-2.22
 2.985 0 1.874.631 2.986 2.229 2.986.623 0 1.254-.249
 1.565-.597v-1.875c-.539.291-.917.44-1.422.44-.664
 0-1.026-.232-1.026-.962s.496-.946 1.026-.946zM3.552
 9.139H0v5.722h3.55v-1.824H1.346v-.688h1.429v-.697H1.346v-.688H3.55z"
 />
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
