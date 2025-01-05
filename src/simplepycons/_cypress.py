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


class CypressIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cypress"

    @property
    def original_file_name(self) -> "str":
        return "cypress.svg"

    @property
    def title(self) -> "str":
        return "Cypress"

    @property
    def primary_color(self) -> "str":
        return "#69D3A7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cypress</title>
     <path d="M11.998.0195c-.8642
 0-1.6816.1101-2.1445.1934v.002C4.1731 1.2283 0 6.1368 0 12.0018c0
 1.1265.1573 2.2328.4648 3.3028.0387.1453.0915.2993.1368.4473 1.607
 4.865 6.2245 8.226 11.3925 8.2285.0651 0
 .2518-.0003.502-.0118.8564-.0353 1.6228-.5734
 1.9512-1.369l.4736-1.1544L20.4258 8.043H18.621l-2.3164
 5.871-2.334-5.871h-1.9082l3.2734 8.0117c-.8115 1.9702-1.6252
 3.9395-2.4355
 5.9101-.0808.1945-.2655.3284-.4727.336-.144.005-.285.0098-.4316.0098-4.5848
 0-8.6672-3.0695-9.9277-7.4649a10.3058 10.3058 0 0
 1-.3985-2.8437c0-5.0887 3.6521-9.3404
 8.6035-10.164.2214-.037.8885-.1446 1.7246-.1446 4.4166 0 8.269 2.732
 9.7305 6.8476.0558.144.0977.293.1465.4395.299.9746.4531 1.9887.4531
 3.0215 0 4.5696-2.9413 8.5326-7.3164 9.8613l.4863 1.5996c5.085-1.546
 8.4995-6.1518 8.502-11.459
 0-1.5491-.2983-2.8706-.6504-3.8926-.0432-.1212-.0873-.2422-.1309-.3633h-.002C21.4577
 3.0954 17.0444.0195 11.998.0195ZM8.4336 7.8906c-1.1999
 0-2.1747.3852-2.9805 1.1758-.8007.7856-1.205 1.7736-1.205 2.9356 0
 1.1544.4068 2.1368 1.205 2.9199.8058.7906 1.7806 1.1738 2.9805 1.1738
 1.705 0 3.1556-.955
 3.7871-2.4883l.0332-.082-1.6289-.5547c-.168.4563-.7552 1.4883-2.1914
 1.4883-.6745
 0-1.2437-.2344-1.6934-.6992-.4572-.4699-.6875-1.0632-.6875-1.7578
 0-.6998.2253-1.2809.6875-1.7735.4522-.4648 1.019-.7012 1.6934-.7012
 1.438 0 2.0238 1.0815 2.1934
 1.4883l1.627-.5527-.0333-.084c-.629-1.5358-2.082-2.4883-3.7871-2.4883Z"
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
