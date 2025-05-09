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


class VowpalWabbitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vowpalwabbit"

    @property
    def original_file_name(self) -> "str":
        return "vowpalwabbit.svg"

    @property
    def title(self) -> "str":
        return "Vowpal Wabbit"

    @property
    def primary_color(self) -> "str":
        return "#FF81F9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vowpal Wabbit</title>
     <path d="M14.872 21.356c.077.195.682 1.646 1.685 2.156 1.075.547
 1.613.406 1.613.406s-.914-3.384-.108-6.076c.807-2.691 1.479-2.933
 1.479-2.933s1.478.591 2.446 0c.968-.591 1.264-1.747
 1.264-1.747s-.672-2.474-1.264-3.442c-.591-.967-1.227-1.48-2.016-1.828a235.34
 235.34 0 0 0-1.508-.655 11.275 11.275 0 0 0-1.003-3.198C16.237 1.531
 14.678 0 14.678 0s-.815.7-1.025 2.032c.56.497 1.462 1.45 2.258
 2.42.4.485.906 1.227 1.31 1.846a26.053 26.053 0 0
 0-2.6-2.626c-1.828-1.586-3.63-2.823-3.63-2.823s-1.29 2.016.243
 4.785c1.048 1.778 3.704 3.31 3.704
 3.31s-2.736.134-3.704.346c-.968.213-2.043.592-3.253
 1.398-1.21.807-2.01 1.647-3.011 3.011-1 1.365-1.962 3.71-1.962
 3.71s-.135-.188-1.049-.188c-.914 0-1.21.188-1.21.188s.027 2.312.592
 3.441c.564 1.13 1.37 1.562 2.392 1.562.27-.002.834 0 .834 0s.699 1.1
 1.129 1.369c.43.268 1.183.215
 1.183.215h8.253s-.048-.619-.51-1.103c-.448-.466-.983-.608-1.117-.666a3.776
 3.776 0 0 0-1.008-.167h-2.123s2.689-.095
 4.274-1.936c.833-.967.914-2.15.833-2.742-.04-.292-.295-1.29-.752-1.882a5.905
 5.905 0 0 0-1.183-1.129c-.516-.36-1.17-.642-1.909-.94 1.075.268
 1.586.376 2.635 1.129 1.048.752 1.505 1.908 1.586
 2.177.08.269.269.672.215 1.828-.108.968-.218 1.208-.484
 1.72-.217.456-.427.742-.717 1.07Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/VowpalWabbit/vowpal_wabbit
/blob/1da1aa4bb4f2dfb5e1a6083c14b429b30eba372d/logo_assets/vowpal-wabb'''

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
