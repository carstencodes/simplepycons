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


class EnvoyProxyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "envoyproxy"

    @property
    def original_file_name(self) -> "str":
        return "envoyproxy.svg"

    @property
    def title(self) -> "str":
        return "Envoy Proxy"

    @property
    def primary_color(self) -> "str":
        return "#AC6199"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Envoy Proxy</title>
     <path d="m23.351 7.593-7.068-4.379a1.034 1.034 0 0
 0-.84-.117c-.02.01-.052.021-.074.032L8.471 6.105a.695.695 0 0
 0-.435.68l.17 7.355c.01.298.191.595.478.765l7.068
 4.38c.255.159.574.201.84.116.02-.01.053-.021.074-.032l6.898-2.976a.705.705
 0 0 0 .436-.68l-.17-7.355c-.011-.297-.192-.584-.479-.765m-7.185
 10.044-6.143-3.805-.149-6.388 5.995-2.583 6.143 3.805.149
 6.388zm.011-6.027a.832.832 0 0 0-.414-.67l-5.06-3.135-.159.064.032
 1.52 4.007 2.487.095 4.06 1.53.946.086-.032zm-6.058 7.132L5.41
 15.83l-.116-4.89 2.146-.924-.042-1.69-3.327 1.435a.611.611 0 0
 0-.382.595l.138 5.74c0 .265.16.52.414.67l5.516
 3.422c.224.138.5.18.734.106a.15.15 0 0 1
 .064-.021l3.252-1.403-1.616-1zm-2.615-6.1-1.52-.947.032 1.446
 1.52.946zm2.19
 5.059-.032-1.414-1.329-.83c-.021-.01-.042-.031-.053-.042l.032
 1.425zm-4.751 1.902-3.476-2.158-.085-3.613 1.7-.734-.031-1.445-2.72
 1.17a.527.527 0 0 0-.33.51l.106 4.336c0 .223.138.446.35.574l4.167
 2.582a.822.822 0 0 0
 .627.096c.021-.01.043-.01.064-.021l2.561-1.106-1.392-.86Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://d33wubrfki0l68.cloudfront.net/6f16455'''

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
