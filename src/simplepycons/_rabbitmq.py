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


class RabbitmqIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rabbitmq"

    @property
    def original_file_name(self) -> "str":
        return "rabbitmq.svg"

    @property
    def title(self) -> "str":
        return "RabbitMQ"

    @property
    def primary_color(self) -> "str":
        return "#FF6600"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>RabbitMQ</title>
     <path d="M23.035 9.601h-7.677a.956.956 0
 01-.962-.962V.962a.956.956 0 00-.962-.956H10.56a.956.956 0
 00-.962.956V8.64a.956.956 0 01-.962.962H5.762a.956.956 0
 01-.961-.962V.962A.956.956 0 003.839 0H.959a.956.956 0
 00-.956.962v22.076A.956.956 0 00.965 24h22.07a.956.956 0
 00.962-.962V10.58a.956.956 0 00-.962-.98zm-3.86 8.152a1.437 1.437 0
 01-1.437 1.443h-1.924a1.437 1.437 0 01-1.436-1.443v-1.917a1.437 1.437
 0 011.436-1.443h1.924a1.437 1.437 0 011.437 1.443z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.rabbitmq.com/trademark-guidelines'''
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
